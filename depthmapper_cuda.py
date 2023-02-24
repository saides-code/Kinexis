import cv2
import numpy as np
import freenect
import pycuda.autoinit
import pycuda.driver as cuda
from pycuda.compiler import SourceModule

# Define some constants
DEPTH_SCALE = 2048  # Maximum depth value for Kinect v1
KERNEL_CODE = """
    __global__ void depth2gray(const uint16_t* depth, uint8_t* gray, const int width, const int height) {
        const int idx = blockIdx.x * blockDim.x + threadIdx.x;
        if (idx < width * height) {
            const uint16_t d = depth[idx];
            const float normalized_d = (float)d / %(depth_scale)s;
            gray[idx] = (uint8_t)(255.0f * normalized_d);
        }
    }
"""

# Initialize the OpenCV window
cv2.namedWindow("Depth Map", cv2.WINDOW_NORMAL)

# Load the CUDA kernel
kernel = SourceModule(KERNEL_CODE % {"depth_scale": DEPTH_SCALE})
depth2gray = kernel.get_function("depth2gray")

# Loop over frames
while True:
    # Get a new depth frame from the Kinect sensor
    depth_data, _ = freenect.sync_get_depth()

    # Convert the depth frame to a grayscale image using CUDA GPU acceleration
    depth_gpu = cuda.mem_alloc(depth_data.nbytes)
    cuda.memcpy_htod(depth_gpu, depth_data)
    gray_gpu = cuda.mem_alloc(depth_data.nbytes // 2)
    depth2gray(depth_gpu, gray_gpu, np.int32(640), np.int32(480), block=(256, 1, 1), grid=((depth_data.size // 2 + 255) // 256, 1, 1))
    gray_data = np.empty_like(depth_data, dtype=np.uint8)
    cuda.memcpy_dtoh(gray_data, gray_gpu)

    # Resize the grayscale image for display
    gray_image = cv2.resize(gray_data, (1920, 1080), interpolation=cv2.INTER_LINEAR)

    # Display the depth map
    cv2.imshow("Depth Map", gray_image)

    # Wait for a key press
    key = cv2.waitKey(1)
    if key == ord("q"):
        break

# Clean up
cv2.destroyAllWindows()

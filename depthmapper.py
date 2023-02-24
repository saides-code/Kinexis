import cv2
import numpy as np
import freenect

# Define some constants
MAX_DEPTH = 4095  # Maximum depth value for Kinect v1
DEPTH_RANGE = 1000  # Maximum range for depth display in mm

# Initialize the OpenCV window
cv2.namedWindow("Depth Map", cv2.WINDOW_NORMAL)

# Set up projector display
projector_width = 1920  # Replace with your projector resolution
projector_height = 1080
projector_display = np.zeros((projector_height, projector_width), dtype=np.uint8)

# Set up CUDA for GPU acceleration
cv2.setUseOptimized(True)
cv2.cuda.setDevice(0)
cuda_depth_map = cv2.cuda_GpuMat(projector_height, projector_width, cv2.CV_8UC1)

# Loop over frames
while True:
    # Get a new depth frame from the Kinect sensor
    depth_frame = freenect.sync_get_depth()[0]

    # Convert the depth frame to a grayscale image
    depth_image = depth_frame.astype(np.uint16)  # Convert to 16-bit unsigned integer
    depth_image = np.clip(depth_image, 0, MAX_DEPTH)  # Clip the values to the range [0, MAX_DEPTH]
    depth_image = depth_image / float(MAX_DEPTH) * DEPTH_RANGE  # Normalize the depth values to the range [0, DEPTH_RANGE]
    depth_image = np.uint8(depth_image)  # Convert back to 8-bit unsigned integer

    # Update the CUDA depth map
    cuda_depth_map.upload(depth_image)
    cuda_depth_map = cv2.cuda.flip(cuda_depth_map, 1)  # Flip horizontally for projector mirroring
    cuda_depth_map = cv2.cuda.cvtColor(cuda_depth_map, cv2.COLOR_GRAY2BGR)  # Convert to 3 channels for projection
    cv2.cuda.warpPerspective(cuda_depth_map, np.eye(3), (projector_width, projector_height),
                              projector_display, cv2.INTER_LINEAR)

    # Display the depth map
    cv2.imshow("Depth Map", depth_image)

    # Display the depth map on the projector screen
    cv2.imshow("Projector Display", projector_display)

    # Wait for a key press
    key = cv2.waitKey(1)
    if key == ord("q"):
        break

# Clean up
cv2.destroyAllWindows()

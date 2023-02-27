import cv2
import numpy as np

# Initialize OpenNI
from openni import openni2
openni2.initialize()

# Set the maximum and minimum depth values to display (in millimeters)
MAX_DEPTH = 1000
MIN_DEPTH = 100

# Open the depth stream
dev = openni2.Device.open_any()
depth_stream = dev.create_depth_stream()
depth_stream.start()

# Create the window
cv2.namedWindow("Depth Map", cv2.WINDOW_FULLSCREEN)

while True:
    # Get the depth map
    frame = depth_stream.read_frame()
    depthmap = np.array(frame.get_buffer_as_uint16()
                        ).reshape(frame.height, frame.width)

    # Apply a Gaussian blur
    depthmap = cv2.GaussianBlur(depthmap, (25, 25), 0)

    # Limit the depth values to the specified range
    depthmap = np.clip(depthmap, MIN_DEPTH, MAX_DEPTH)

    # Normalize the depth map
    depthmap = cv2.normalize(depthmap, None, 255, 0,
                             cv2.NORM_MINMAX).astype(np.uint8)

    # Invert the depth map
    depthmap = cv2.bitwise_not(depthmap)

    # Display the depth map
    cv2.imshow("Depth Map", depthmap)

    # Check for user input
    key = cv2.waitKey(1)
    if key == 27:  # Esc key
        break

# Release the resources
depth_stream.stop()
cv2.destroyAllWindows()
openni2.unload()

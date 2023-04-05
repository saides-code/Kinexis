import cv2
import numpy as np
import datetime

# Initialize OpenNI
from openni import openni2
openni2.initialize()

# Set the maximum and minimum depth values to display (in millimeters)
MAX_DEPTH = 10000
MIN_DEPTH = 100

toggle_switch = True  # Define toggle switch here

# Open the depth and color streams
dev = openni2.Device.open_any()
depth_stream = dev.create_depth_stream()
color_stream = dev.create_color_stream()

# Set the video modes for the streams
color_stream.set_video_mode(openni2.VideoMode(pixelFormat=openni2.PIXEL_FORMAT_RGB888, resolutionX=1280, resolutionY=960, fps=30))
depth_stream.set_video_mode(openni2.VideoMode(pixelFormat=openni2.PIXEL_FORMAT_DEPTH_1_MM, resolutionX=640, resolutionY=480, fps=30))

depth_stream.start()
color_stream.start()

# Create the window
cv2.namedWindow("Color Map", cv2.WINDOW_NORMAL)

# Define the output directory
output_dir = './out/'

# Create trackbars
cv2.createTrackbar("Min Depth", "Color Map", MIN_DEPTH, MAX_DEPTH, lambda x: None)
cv2.createTrackbar("Max Depth", "Color Map", MAX_DEPTH, MAX_DEPTH, lambda x: None)

while True:
    # Get the depth map and color map
    depth_frame = depth_stream.read_frame()
    color_frame = color_stream.read_frame()
    depth_map_raw = np.array(depth_frame.get_buffer_as_uint16()).reshape(depth_frame.height, depth_frame.width)
    color_map_raw = np.array(color_frame.get_buffer_as_triplet()).reshape(color_frame.height, color_frame.width, 3)

    # Limit the depth values to the specified range
    min_depth = cv2.getTrackbarPos("Min Depth", "Color Map")
    max_depth = cv2.getTrackbarPos("Max Depth", "Color Map")
    depth_map = np.clip(depth_map_raw, min_depth, max_depth)

    # Normalize the depth map
    depth_map_norm = cv2.normalize(depth_map, None, 255, 0, cv2.NORM_MINMAX).astype(np.uint8)

    # Invert the depth map if toggle switch is on
    if toggle_switch:
        depth_map_norm = cv2.bitwise_not(depth_map_norm)

    # Create a preview image with depth overlay
    preview = color_map_raw.copy()

    # Apply color correction to the color map
    color_map_raw_corr = cv2.cvtColor(color_map_raw, cv2.COLOR_RGB2BGR)

    # Resize depth_map_norm to match the dimensions of color_map_raw_corr
    depth_map_norm_resized = cv2.resize(depth_map_norm, (color_map_raw_corr.shape[1], color_map_raw_corr.shape[0]))
    
    # Apply blur effect to the depth map
    depth_map_norm_resized_blurred = cv2.GaussianBlur(depth_map_norm_resized, (5, 5), 0)

    depth_map_processed = depth_map_norm_resized_blurred

    # Create a heatmap overlay
    heatmap = cv2.applyColorMap(depth_map_processed, cv2.COLORMAP_JET)
    heatmap_alpha = 0.5
    preview = cv2.addWeighted(preview, 1 - heatmap_alpha, heatmap, heatmap_alpha, 0)

    # Show the preview image
    cv2.imshow("Color Map", preview)

    # Save the raw depth channel and color-corrected raw color channel when 's' is pressed
    key = cv2.waitKey(1) & 0xFF
    if key == ord('s'):
        filename_depth = output_dir + datetime.datetime.now().strftime("%Y%m%d_%H%M%S") + '_depth.tif'
        filename_color = output_dir + datetime.datetime.now().strftime("%Y%m%d_%H%M%S") + '_color.tif'
        min_depth = cv2.getTrackbarPos("Min Depth", "Color Map")
        max_depth = cv2.getTrackbarPos("Max Depth", "Color Map")
    
        # Convert the grayscale depth map to a BGR image for saving
        depth_map_bgr = cv2.cvtColor(depth_map_processed, cv2.COLOR_GRAY2BGR)
    
        # Save the clipped grayscale depth map and color-corrected color map
        cv2.imwrite(filename_depth, depth_map_bgr)
        cv2.imwrite(filename_color, color_map_raw_corr)


    # Toggle the invert switch when 'i' is pressed
    elif key == ord('i'):
        toggle_switch = not toggle_switch

    # Exit the program when 'q' is pressed
    elif key == ord('q'):
        break

# Stop the streams and close the window
depth_stream.stop()
color_stream.stop()
cv2.destroyAllWindows()

import cv2
import numpy as np

# Load image and convert to grayscale
input_image = cv2.imread('sample-images/angrybird.png')
gray_image = cv2.cvtColor(input_image, cv2.COLOR_BGR2GRAY)

# Save the grayscale image
cv2.imwrite('v2_2d_gray_img.png', gray_image)

# Perform edge detection on the grayscale image
edges = cv2.Canny(gray_image, threshold1=50, threshold2=150)

# Find contours in the edges
contours, _ = cv2.findContours(edges, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

# Define servo coordinate limits
servo_x_min = 0
servo_x_max = 180
servo_y_min = 0
servo_y_max = 180
servo_z_min = 0
servo_z_max = 180

# Initialize and configure your servo control library
# servo_x = ...
# servo_y = ...
# servo_z = ...

servo_z_down = 0
servo_z_up = 180

# Define the threshold for pen up or down
threshold_value = 1000  # Adjust this value based on your image and setup

# Initialize a list to store servo coordinates
servo_coordinates = []

# Convert contours to servo coordinates and save to a list
for contour in contours:
    # Calculate centroid of contour
    M = cv2.moments(contour)
    if M["m00"] != 0:
        cX = int(M["m10"] / M["m00"])
        cY = int(M["m01"] / M["m00"])
        
        # Map centroid to servo coordinates
        servo_x = np.interp(cX, [0, gray_image.shape[1]], [servo_x_min, servo_x_max])
        servo_y = np.interp(cY, [0, gray_image.shape[0]], [servo_y_min, servo_y_max])
        
        # Determine pen up or down based on contour area
        contour_area = cv2.contourArea(contour)
        if contour_area > threshold_value:
            servo_z = servo_z_down  # Lower the pen
        else:
            servo_z = servo_z_up  # Raise the pen
        
        # Append servo coordinates to the list
        # servo_coordinates.append((servo_x, servo_y, servo_z))
        servo_coordinates.append((round(servo_x, 2), round(servo_y, 2), round(servo_z, 2)))


# Save servo coordinates to a text file
with open('v2_2d_servoCords.txt', 'w') as f:
    for i, coords in enumerate(servo_coordinates, start=1):
        # f.write(f"Contour {i}: X: {coords[0]}, Y: {coords[1]}, Z: {coords[2]}\n")
        f.write(f"{coords[0]}, {coords[1]}, {coords[2]}\n")


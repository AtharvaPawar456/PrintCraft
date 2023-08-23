import cv2
import numpy as np

# Load image and perform edge detection
image = cv2.imread('sample-images/angrybird.png', cv2.IMREAD_GRAYSCALE)
edges = cv2.Canny(image, threshold1=50, threshold2=150)

# Find contours in the edges
contours, _ = cv2.findContours(edges, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

# Define servo coordinate limits
servo_x_min = 0
servo_x_max = 270
servo_y_min = 0
servo_y_max = 270
servo_z_min = 0
servo_z_max = 270

# Convert contours to servo coordinates
servo_coordinates = []
for contour in contours:
    # Calculate centroid of contour
    M = cv2.moments(contour)
    if M["m00"] != 0:
        cX = int(M["m10"] / M["m00"])
        cY = int(M["m01"] / M["m00"])
        
        # Map centroid to servo coordinates
        servo_x = np.interp(cX, [0, image.shape[1]], [servo_x_min, servo_x_max])
        servo_y = np.interp(cY, [0, image.shape[0]], [servo_y_min, servo_y_max])
        servo_z = np.interp(len(contour), [0, 500], [servo_z_min, servo_z_max])  # Example mapping contour length to Z coordinate
        
        servo_coordinates.append((round(servo_x, 2), round(servo_y, 2), round(servo_z, 2)))

# Save grayscale image
cv2.imwrite('gray_img_2D.jpg', image)

# Save servo coordinates to a text file
with open('servo_cord_2D.txt', 'w') as f:
    # f.write("Servo Coordinates: X, Y, Z\n")
    for i, coords in enumerate(servo_coordinates, start=1):
        # f.write(f"Contour {i}: X: {coords[0]}, Y: {coords[1]}, Z: {coords[2]}\n")
        f.write(f"{coords[0]}, {coords[1]}, {coords[2]}\n")

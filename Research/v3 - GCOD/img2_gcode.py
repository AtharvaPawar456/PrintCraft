import cv2
import numpy as np

# Load input image and convert to grayscale
input_image = cv2.imread('sample-images/angrybird.png', cv2.IMREAD_GRAYSCALE)

# Perform edge detection on the grayscale image
edges = cv2.Canny(input_image, threshold1=50, threshold2=150)

# Find contours in the edges
contours, _ = cv2.findContours(edges, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

# Define CNC machine parameters
steps_per_mm = 10  # Adjust this value based on your CNC machine
feed_rate = 100    # Adjust this value based on your CNC machine

# Generate G-code commands
gcode_commands = []

for contour in contours:
    gcode_commands.append("G1 Z10")  # Lift pen
    for point in contour:
        x = point[0][0] / steps_per_mm
        y = point[0][1] / steps_per_mm
        gcode_commands.append(f"G1 X{x:.3f} Y{y:.3f} F{feed_rate}")  # Move to contour point
        gcode_commands.append("G1 Z0")  # Lower pen

# Save G-code commands to a text file
with open('output_gcode.txt', 'w') as f:
    for command in gcode_commands:
        f.write(command + '\n')

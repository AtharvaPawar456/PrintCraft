# Working

# Libraries
import numpy as np

# Load OBJ file
obj_file_path = 'dog_sample/10680_Dog_v2.obj'  # Replace with your OBJ file path
vertices = []

with open(obj_file_path, 'r') as f:
    for line in f:
        if line.startswith('v '):
            parts = line.split()
            vertex = [float(parts[1]), float(parts[2]), float(parts[3])]
            vertices.append(vertex)

# Define the dimensions of the 6x6x6 area
area_size = 6.0

# Define servo angle ranges (in degrees)
servo1_range = (0, 180)  # Example ranges, adjust based on your servo specifications
servo2_range = (0, 180)
servo3_range = (0, 180)

# Calculate normalized coordinates and map to servo angles
def convert_to_servo_coordinates(vertex):
    x, y, z = vertex
    servo1_angle = np.interp(x, [0, area_size], servo1_range)
    servo2_angle = np.interp(y, [0, area_size], servo2_range)
    servo3_angle = np.interp(z, [0, area_size], servo3_range)
    return round(servo1_angle, 2), round(servo2_angle, 2), round(servo3_angle, 2)

# Convert each vertex to servo coordinates
servo_coordinates = []
for vertex in vertices:
    servo_angles = convert_to_servo_coordinates(vertex)
    servo_coordinates.append(servo_angles)

# Export servo coordinates to a file
output_file_path = 'servo_coordinates_OBJ.txt'
with open(output_file_path, 'w') as f:
    for angles in servo_coordinates:
        f.write(f'{angles[0]}, {angles[1]}, {angles[2]}\n')

print(f'Servo coordinates exported to {output_file_path}')


'''
Input:
0.0, 180.0, 180.0
0.0, 179.22, 180.0
0.0, 179.97, 180.0
0.0, 180.0, 180.0
0.0, 171.58, 180.0
0.0, 165.33, 180.0
0.0, 166.18, 180.0
0.0, 172.37, 180.0

Output:
0  --  1073525264  --  0  --   
------------
0  --  1073525264  --  0  --   
------------
0  --  1073525264  --  0  --   
------------
0  --  1073525264  --  0  --   

'''
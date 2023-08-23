import numpy as np
from stl import mesh

# Load STL file
stl_file_path = 'dog_sample/path_to_your_model.stl'
mesh_data = mesh.Mesh.from_file(stl_file_path)

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
    return servo1_angle, servo2_angle, servo3_angle

# Convert each vertex to servo coordinates
servo_coordinates = []
for vertex in mesh_data.vectors.reshape(-1, 3):
    servo_angles = convert_to_servo_coordinates(vertex)
    servo_coordinates.append(servo_angles)

# Export servo coordinates to a file
output_file_path = 'servo_coordinates_STL.txt'
with open(output_file_path, 'w') as f:
    for angles in servo_coordinates:
        f.write(f'{angles[0]}, {angles[1]}, {angles[2]}\n')

print(f'Servo coordinates exported to {output_file_path}')

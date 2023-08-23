# Read servo coordinates from the text file
servo_coordinates = []
with open('v4_servoCords.txt', 'r') as f:
    for line in f:
        coords = line.strip().split(', ')
        servo_coordinates.append((float(coords[0]), float(coords[1]), float(coords[2])))

# Remove duplicate rows and keep only 2 occurrences
unique_servo_coordinates = []
prev_coords = None
duplicate_count = 0

for coords in servo_coordinates:
    if coords != prev_coords:
        unique_servo_coordinates.append(coords)
        prev_coords = coords
        duplicate_count = 1
    else:
        duplicate_count += 1
        if duplicate_count <= 2:
            unique_servo_coordinates.append(coords)

# Save filtered servo coordinates to a new text file
with open('filtered_v4_2d_servoCords.txt', 'w') as f:
    for i, coords in enumerate(unique_servo_coordinates, start=1):
        # f.write(f"Point {i}: X: {coords[0]}, Y: {coords[1]}, Z: {coords[2]}\n")
        f.write(f"{coords[0]}, {coords[1]}, {coords[2]}\n")


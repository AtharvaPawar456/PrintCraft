import cv2
import numpy as np
import os

# Define the folder paths
testCodeFolder = 'uploads'
servoCods = "uploads\setup\servoCords.txt"

# Function to process the uploaded image
def processImage():
    # Get the list of filenames in the folder
    image_filenames = listFileinFolder(testCodeFolder)
    if 'gray_img.png' not in image_filenames:

        # Load input image and convert to grayscale
        input_image = cv2.imread(f'uploads/{image_filenames[0]}')
        gray_image = cv2.cvtColor(input_image, cv2.COLOR_BGR2GRAY)

        # Save the grayscale image
        cv2.imwrite('uploads/gray_img.png', gray_image)

        # Perform edge detection on the grayscale image
        edges = cv2.Canny(gray_image, threshold1=50, threshold2=150)

        # Save the grayscale image
        cv2.imwrite('uploads/img_edges.png', edges)

        # Find contours in the edges
        contours, _ = cv2.findContours(edges, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

        # Define servo coordinate limits
        servo_x_min = 0
        servo_x_max = 180
        servo_y_min = 0
        servo_y_max = 180
        servo_z_min = 0
        servo_z_max = 180

        servo_z_down = 0
        servo_z_up = 180

        # Define the threshold for pen up or down
        threshold_value = 1000  # Adjust this value based on your image and setup

        # Initialize a list to store servo coordinates
        servo_coordinates = []

        # Convert contours to servo coordinates and save to a list
        for contour in contours:
            # Sample points along the contour
            num_points = 100  # Number of points to sample
            contour_points = np.linspace(0, 1, num_points)
            
            # Convert contours to servo coordinates and save to a list
            for t in contour_points:
                idx = int(t * (len(contour) - 1))  # Ensure index is within bounds
                pt = contour[idx][0]
                cX, cY = pt
                
                # Map contour point to servo coordinates
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
        with open(servoCods, 'w') as f:
            for i, coords in enumerate(servo_coordinates, start=1):
                f.write(f"{coords[0]}, {coords[1]}, {coords[2]}\n")
        cleanCods()

    else:
        print("gray_img images present!!!")


def cleanCods():
    # Read servo coordinates from the text file
    servo_coordinates = []
    with open(servoCods, 'r') as f:
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
    with open(servoCods, 'w') as f:
        for i, coords in enumerate(unique_servo_coordinates, start=1):
            # f.write(f"Point {i}: X: {coords[0]}, Y: {coords[1]}, Z: {coords[2]}\n")
            f.write(f"{coords[0]}, {coords[1]}, {coords[2]}\n")

def DeleteAllFiles(testCodeFolder):
    folder_path = testCodeFolder
    try:
        # List all files in the folder
        file_list = os.listdir(folder_path)

        # Delete each file
        for file_name in file_list:
            file_path = os.path.join(folder_path, file_name)
            try:
                if os.path.isfile(file_path):
                    os.remove(file_path)
                    print(f"Deleted file: {file_name}")
            except Exception as e:
                print(f"Error deleting file {file_name}: {e}")
    except Exception as e:
        print(f"Error listing files in {folder_path}: {e}")

def listFileinFolder(testCodeFolder):
    # List all files in the folder
    file_list = os.listdir(testCodeFolder)
    filesnames = []
    # Print the list of file names
    for file_name in file_list:
        filesnames.append(file_name)
        # print(file_name)
    return filesnames

def display_all_content(file_name):
    # file_path = os.path.join(settings.MEDIA_ROOT, 'uploads', file_name)
    file_path = servoCods
    try:
        with open(file_path, 'r') as file:
            file_content = file.read()
    except FileNotFoundError:
        file_content = "File not found."

    data = {
        "file_name": file_name,
        "file_content": file_content,
    }
    return data

def display_10percent_file_content(file_name):
    file_path = servoCods
    try:
        with open(file_path, 'r') as file:
            full_file_content = file.read()
            content_length = len(full_file_content)
            ten_percent = int(content_length * 0.1)
            file_content = full_file_content[:ten_percent]
    except FileNotFoundError:
        file_content = "File not found."

    data = {
        "file_name": file_name,
        "file_content": file_content,
    }
    return data
# print(listFileinFolder())
# print(processImage())

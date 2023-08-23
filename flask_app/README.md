# PrintCraft: Online 2D Printer Servo Coordinates Generator and Marker

![PrintCraft Logo](https://github.com/AtharvaPawar456/PrintCraft/blob/main/Website_flask_half_version_1.0/static/PrintCraft-logo.png)

PrintCraft is an innovative online 2D printer Servo Coordinates Generator and Marker application developed by Atharva Pawar. This project aims to bridge the gap between digital images and physical 2D prints by leveraging edge detection algorithms and servo control technology. By providing users with a user-friendly interface, PrintCraft empowers users to transform their digital images into tangible creations through the coordination of servo motors.

![IoT : ESP32 Simulation](https://github.com/AtharvaPawar456/PrintCraft/blob/main/flask_app/static/iot-simulation.jpeg)

## Table of Contents
- [Introduction](#introduction)
- [Features](#features)
- [Getting Started](#getting-started)
- [Usage](#usage)
- [Technologies Used](#technologies-used)
- [Installation](#installation)
- [Contributions](#contributions)
- [License](#license)
- [Acknowledgements](#acknowledgements)

## Introduction

PrintCraft is a unique web application designed to facilitate the conversion of digital images into physical 2D prints using servo motor coordination. The application's backend, built using the Flask web framework, processes uploaded images, performs grayscale conversion, applies edge detection techniques, and generates precise servo coordinates for each point on the detected edges.

## Features

- **Image Upload:** Users can upload images in various formats, including PNG, JPG, JPEG, and GIF.

- **Grayscale Conversion:** Uploaded images are automatically transformed into grayscale, preparing them for edge detection.

- **Edge Detection:** The application utilizes edge detection algorithms to identify significant edges within the grayscale image.

- **Servo Coordinate Generation:** Based on the identified edges, PrintCraft generates servo coordinates for precise 2D printing.

- **Interactive Interface:** A user-friendly web interface enables users to upload images, view grayscale versions, and examine generated servo coordinates.

- **Coordinate Display:** Users can easily view and download the servo coordinates in a clear and structured format.

- **Image Deletion:** Uploaded images and associated data can be efficiently deleted, ensuring a clutter-free workspace.

## Getting Started

To get started with PrintCraft, follow these steps:

Website Deployed Link : `https://printcraft.atharvapawar.repl.co/` 

1. Clone the repository: `git clone https://github.com/AtharvaPawar456/PrintCraft.git`

2. Navigate to the project directory: `cd PrintCraft`

3. Install the required dependencies: `pip install -r requirements.txt`

4. Run the Flask development server: `python app.py`

5. Access the application through your web browser: `http://localhost:5000`

## Usage

1. Upload an image through the intuitive web interface.

2. The application will convert the image to grayscale and perform edge detection.

3. Servo coordinates for 2D printing will be generated based on the detected edges.

4. View and download the servo coordinates for your printing needs.

5. Repeat the process for new images or modify the existing workflow.

## Technologies Used

- Flask: A lightweight and flexible web framework for building web applications.

- OpenCV: A powerful computer vision library used for image processing and edge detection.

- ESP32Servo: A library for controlling servo motors in Arduino-based projects.

- HTML, CSS, JavaScript: Frontend technologies for creating a responsive and interactive user interface.

## Installation

1. Install Python: Download and install Python from [python.org](https://www.python.org/downloads/).

2. Clone the repository: `git clone https://github.com/AtharvaPawar456/PrintCraft.git`

3. Navigate to the project directory: `cd PrintCraft`

4. Install required dependencies: `pip install -r requirements.txt`

5. Run the application: `python app.py`

6. Access the application through your web browser at `http://localhost:5000`.

## Basic pip cmds
    ```
    pip freeze > requirements.txt
    
    pip install -r requirements.txt
    
    pip uninstall -r requirements.txt
    ```

# Utils.py
    - cleanCods():
            Reads servo coordinates from a text file.
            Removes duplicate rows while keeping only 2 occurrences.
            Saves the filtered servo coordinates to a new text file.

    - DeleteAllFiles(testCodeFolder):
            Deletes all files in a specified folder.
            Lists files in the folder.
            Deletes each file, if it exists.

    - listFileinFolder(testCodeFolder):
            Lists all files in a specified folder.
            Creates a list of filenames.
            Returns the list of filenames.

    - display_all_content(file_name):
            Constructs the full file path based on servoCods.
            Attempts to open the file and read its content.
            If the file is not found, a default message is provided.
            Creates a dictionary containing the file name and its full content or a default message.

    - display_10percent_file_content(file_name):
            Constructs the full file path based on servoCods.
            Attempts to open the file and read its full content.
            Calculates 10% of the content length.
            Extracts the first 10% of the content.
            If the file is not found, a default message is provided.
            Creates a dictionary containing the file name and its 10% content or a default message.

## Contributions

Contributions to PrintCraft are welcome! If you find any issues or have suggestions for enhancements, please feel free to create a pull request or open an issue.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Acknowledgements

Special thanks to the open-source community for providing valuable libraries and tools that have contributed to the development of PrintCraft.

## Contact

For inquiries and support, please contact Atharva Pawar at talktoatharva14@gmail.com.

---
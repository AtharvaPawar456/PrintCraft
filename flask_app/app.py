# PrintCraft : Online 3D Printer

# Import necessary modules
import os
from flask import Flask, request, render_template, send_from_directory
from werkzeug.utils import secure_filename
from utils import processImage, DeleteAllFiles, listFileinFolder, display_all_content, display_10percent_file_content

# Create a Flask app instance
app = Flask(__name__)

# Set the folder where uploaded files will be stored
UPLOAD_FOLDER = 'uploads'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

# Define the test code folder path
testCodeFolder = app.config['UPLOAD_FOLDER'] 
# print("testCodeFolder: ", testCodeFolder)

# Define allowed file extensions
ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg', 'gif'}

# Function to check if a file has an allowed extension
def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

# Route for handling file uploads and processing
@app.route('/', methods=['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
        if 'file' not in request.files:
            return "No file part"
        
        file = request.files['file']
        
        if file.filename == '':
            return "No selected file"
        
        if file:
            # Delete existing files and process the uploaded image
            DeleteAllFiles(testCodeFolder)

            filename = secure_filename(file.filename)
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
            processImage()

            # Create a list of image data for rendering
            image_data = []
            for filename in os.listdir(app.config['UPLOAD_FOLDER']):
                if allowed_file(filename):
                    image_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
                    image_data.append({'filename': filename, 'image_path': image_path})

            # Display servo cods
            servoCods = "uploads\setup"
            filenames = listFileinFolder(servoCods)
            fileData = []
            for file_item in filenames:
                result = display_10percent_file_content(file_item)
                fileData.append(result)

            # Prepare parameters for rendering the template
            params = { 
                "msg" : "File uploaded successfully", 
                "uploaded_images" : image_data,
                "filenames": filenames,
                "fileData": fileData, 
                }
            return render_template('upload.html', params=params)
    
    params = { "msg" : "File uploaded successfully"}       
    return render_template('upload.html',  params=params)

# Route for serving uploaded files
@app.route('/uploads/<filename>')
def uploaded_file(filename):
    return send_from_directory(app.config['UPLOAD_FOLDER'], filename)

# Route for displaying uploaded images
@app.route('/display')
def display_images():
    # Get the list of uploaded image files
    uploaded_images = os.listdir(app.config['UPLOAD_FOLDER'])

    # Create a list of image data for rendering
    image_data = []
    for filename in os.listdir(app.config['UPLOAD_FOLDER']):
        if allowed_file(filename):
            image_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
            image_data.append({'filename': filename, 'image_path': image_path})
    
    return render_template('display.html', uploaded_images=uploaded_images)

# Route for displaying full content of servo cords
@app.route('/fullcontent')
def fullcontent():
    # Define the path to the folder containing servo cords
    servoCods = "uploads\setup"

    # Get a list of file names in the servo cords folder
    filenames = listFileinFolder(servoCods)

    # Create a list to store content data for rendering
    fileData = []
    for file_item in filenames:
        result = display_all_content(file_item)
        fileData.append(result)

    # Prepare parameters for rendering the template
    params = { "content" : fileData}
    return render_template('fullcontent.html',params=params)

# Run the app if executed as the main script
if __name__ == '__main__':
    app.run(debug=True)

import os
import cv2
from AddDatatodatabase import data as data_adder
# Path to the directory containing the images
directory_path = "/Users/jusvanthraja/Downloads/Ex1/FaceAttendenceSystem/Images"

# Path to the directory where you want to save the processed images
output_directory = "/Users/jusvanthraja/Downloads/Ex1/FaceAttendenceSystem/Images"

# List all files in the directory
file_list = os.listdir(directory_path)

# Iterate through each file in the directory
for file_name in file_list:
    # Construct the full path to the input image file
    input_file_path = os.path.join(directory_path, file_name)
    
    # Check if the file is an image file
    if file_name.endswith('.png') or file_name.endswith('.jpg') or file_name.endswith('.jpeg'):
        # Load the input image
        img = cv2.imread(input_file_path)
        
        # Check if the image is loaded successfully
        if img is not None:
            # Process the image (e.g., resize, apply operations, etc.)
            # For example, resizing the image to custom dimensions
            custom_width = 216
            custom_height = 216
            resized_img = cv2.resize(img, (custom_width, custom_height))
            
            # Construct the full path to the output image file
            output_file_path = os.path.join(output_directory, file_name)
            
            # Save the processed image to the output directory
            cv2.imwrite(output_file_path, resized_img)
            
            print(f"Processed image saved: {output_file_path}")
        else:
            print(f"Failed to load input image file: {input_file_path}")
    else:
        print(f"Skipping non-image file: {input_file_path}")


def addData(data):
    data_adder[data] = {
            "name": "Daniel Prince D",
            "major": "computerscience",
            "starting_year": 2021,
            "total_attendance": 12,
            "standing": "B",
            "year": 1,
            "last_attendance_time": "2022-12-11 00:54:34"
        }

addData("21CS022")
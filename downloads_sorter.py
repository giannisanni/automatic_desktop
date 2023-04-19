import os
import shutil
import time

# Set up the folder to watch and destination folder
folder_to_track = r"/home/gianni/Downloads/"
folder_destination = r"/home/gianni/Downloads/"

# Define a dictionary of file types to watch for and their corresponding categories
file_extensions = {
    "jpg": "Images",
    "jpeg": "Images",
    "png": "Images",
    "gif": "Images",
    "bmp": "Images",
    "svg": "Images",
    "mp4": "Videos",
    "avi": "Videos",
    "wmv": "Videos",
    "mov": "Videos",
    "mkv": "Videos",
    "mp3": "Music",
    "wav": "Music",
    "aac": "Music",
    "pdf": "Documents",
    "doc": "Documents",
    "docx": "Documents",
    "xls": "Documents",
    "xlsx": "Documents",
    "ppt": "Documents",
    "pptx": "Documents",
    "txt": "Text",
    "zip": "Archives",
    "rar": "Archives",
    "7z": "Archives",
    "py": "Code",
    "cpp": "Code",
    "c": "Code",
    "java": "Code",
    "html": "Code",
    "css": "Code",
    "js": "Code",
    "php": "Code",
    "sh": "Code",
    "ipynb": "Code"
}

def create_folders(destination_folder):
    """Create folders for each category in the given directory."""
    for category in set(file_extensions.values()):
        folder_name = f"{destination_folder}/{category}"
        if not os.path.exists(folder_name):
            os.makedirs(folder_name)

def move_files():
    # Create folders for each category in the destination folder
    create_folders(folder_destination)

    # Move files to the appropriate folder
    files = os.listdir(folder_to_track)
    for filename in files:
        source = os.path.join(folder_to_track, filename)
        if os.path.isfile(source):
            # Determine the category based on the file extension
            file_extension = filename.split(".")[-1].lower()
            category = file_extensions.get(file_extension, file_extension.capitalize())
            destination_folder = f"{folder_destination}/{category}"
            if not os.path.exists(destination_folder):
                os.makedirs(destination_folder)
            destination = os.path.join(destination_folder, filename)

            # Move the file to the destination folder
            try:
                shutil.move(source, destination)
            except (shutil.Error, OSError):
                # If there's an error moving the file, skip it
                pass

if __name__ == "__main__":
    while True:
        move_files()
        time.sleep(10) # Wait for 10 seconds before checking again



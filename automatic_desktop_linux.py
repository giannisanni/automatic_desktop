import os
import time
from watchdog.events import FileSystemEventHandler
from watchdog.observers import Observer
import shutil

# Set up the folder to watch and destination folder
folder_to_track = r"/home/gianni/Desktop/myFolder/"
folder_destination = r"/home/gianni/Desktop/newfolder/"

# Define a list of file types to watch for
FILE_TYPES = ["jpg", "png", "gif", "pdf", "doc", "docx", "xls", "xlsx", "ppt", "pptx"]

def create_folders(destination_folder):
    """Create folders for each file type in the given directory."""
    for file_type in FILE_TYPES:
        folder_name = f"{destination_folder}/DOWNLOADS({file_type.upper()})"
        if not os.path.exists(folder_name):
            os.makedirs(folder_name)

class MoveHandler(FileSystemEventHandler):
    def __init__(self, folder_to_track, folder_destination):
        self.folder_to_track = folder_to_track
        self.folder_destination = folder_destination

    def on_modified(self, event):
        # Create folders for each file type in the destination folder
        create_folders(self.folder_destination)

        # Move files to the appropriate folder
        dir1 = os.listdir(self.folder_to_track)
        for filename in dir1:
            source = os.path.join(self.folder_to_track, filename)
            if os.path.isfile(source):
                # Determine the file type
                file_type = filename.split(".")[-1]
                if file_type in FILE_TYPES:
                    destination_folder = f"{self.folder_destination}/DOWNLOADS({file_type.upper()})"
                    destination = os.path.join(destination_folder, filename)

                    # Wait for the file to finish copying before moving it
                    file_done = False
                    file_size = -1

                    while not file_done:
                        try:
                            # Move the file to the destination folder
                            shutil.move(source, destination)
                            file_done = True
                        except (shutil.Error, OSError) as e:
                            # If the file is still being written, wait for a short period before retrying
                            if "same file" in str(e):
                                time.sleep(1)
                            # If the file is locked, wait for a short period before retrying
                            elif os.path.exists(destination):
                                time.sleep(1)
                            # If the file doesn't exist, exit the loop
                            else:
                                file_done = True

folder_to_track = r"/home/gianni/Desktop/myFolder/"
folder_destination = r"/home/gianni/Desktop/newfolder/"
event_handler = MoveHandler(folder_to_track, folder_destination)
observer = Observer()
observer.schedule(event_handler, folder_to_track, recursive=True)
observer.start()
try:
    while True:
        time.sleep(1)
except KeyboardInterrupt:
    observer.stop()
observer.join()



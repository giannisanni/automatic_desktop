import os
import time
from watchdog.events import FileSystemEventHandler
from watchdog.observers import Observer
import shutil


class MoveHandler(FileSystemEventHandler):
    def __init__(self, folder_to_track, folder_destination, file_extensions):
        self.folder_to_track = folder_to_track
        self.folder_destination = folder_destination
        self.file_extensions = file_extensions

    def on_modified(self, event):
        dir1 = os.listdir(self.folder_to_track)
        for filename in dir1:
            source = os.path.join(self.folder_to_track, filename)
            destination = os.path.join(self.folder_destination, filename)

            if os.path.isfile(source):
                ext = os.path.splitext(filename)[1]
                if ext.lower() in self.file_extensions:
                    file_done = False
                    file_size = -1

                    while file_size != os.path.getsize(source):
                        file_size = os.path.getsize(source)
                        time.sleep(1)

                    while not file_done:
                        try:
                            shutil.move(source, destination)
                            file_done = True
                        except (Exception, ):
                            return True


folder_to_track = r"/home/gianni/Desktop/myFolder/"
folder_destination = r"/home/gianni/Desktop/newfolder/"
file_extensions = [".jpg", ".png", ".pdf"]  # Add any file extensions you want to move here
event_handler = MoveHandler(folder_to_track, folder_destination, file_extensions)
observer = Observer()
observer.schedule(event_handler, folder_to_track, recursive=True)
observer.start()
try:
    while True:
        time.sleep(10)
except KeyboardInterrupt:
    observer.stop()
observer.join()



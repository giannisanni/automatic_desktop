import os
import time
from watchdog.events import FileSystemEventHandler
from watchdog.observers import Observer
import shutil


class MoveHandler(FileSystemEventHandler):
    def on_modified(self, event):
        dir1 = os.listdir(folder_to_track)
        for filename in dir1:
            filename1 = filename
            filename2 = filename
            source = folder_to_track + "//" + filename1
            new_destination = folder_destination + "//" + filename2
            file_done = False
            file_size = -1

            while file_size != os.path.getsize(folder_to_track):
                file_size = os.path.getsize(folder_destination)
                time.sleep(1)

            while not file_done:
                try:
                    os.rename(source, new_destination)
                    file_done = True
                except (Exception, ):
                    return True


folder_to_track = r"/home/gianni/Desktop/myFolder/"
folder_destination = r"/home/gianni/Downloads/"
event_handler = MoveHandler()
observer = Observer()
observer.schedule(event_handler, folder_to_track, recursive=True)
observer.start()
try:
    while True:
        time.sleep(10)
except KeyboardInterrupt:
    observer.stop()
observer.join()

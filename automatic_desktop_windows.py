import os
import shutil
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

sourcepath = 'C:/Users/gianni/Downloads/'

destinationpath = {
    '.xls': 'C:/Users/gianni/Downloads/xls',
    '.xlsx': 'C:/Users/gianni/Downloads/xls',
    '.csv': 'C:/Users/gianni/Downloads/csv',
    '.txt': 'C:/Users/gianni/Downloads/txt',
    '.pdf': 'C:/Users/gianni/Downloads/pdf',
}

def move_it(event):
    # print(dir(event))
    # print('event:', event)
    # print('event_type:', event.event_type)
    # print('is_directory:', event.is_directory)
    # print('src_path:', event.src_path)
    # print('key:', event.key)
    # print('----')
    if not event.is_directory:

        parts = os.path.split(event.src_path)
        # print('parts:', parts)
        filename = parts[-1]

        for ext, dst in destinationpath.items():
            if filename.lower().endswith(ext):
                shutil.move(event.src_path, os.path.join(dst, filename))
                print('move:', filename, '->', dst)


if __name__ == "__main__":

    try:
        event_handler = FileSystemEventHandler()
        event_handler.on_modified = move_it
        event_handler.on_created = move_it
        # event_handler.on_moved    = move_it  # ie. rename (but this needs to check `dest_path`)

        observer = Observer()
        observer.start()
        observer.schedule(event_handler, sourcepath, recursive=True)
        observer.join()
    except KeyboardInterrupt:
        print('Stopped by Ctrl+C')

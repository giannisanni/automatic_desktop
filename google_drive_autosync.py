import shutil
import time
import os

# Set the source and destination paths
src = '/run/media/gianni/Extreme SSD/obsidian_vault/'
dest = '/home/gianni/local_vault'

while True:
    try:
        # Move the contents of the source folder to the destination folder
        shutil.move(src, dest)
        print(f"Moved contents of {src} to {dest}")

        # Wait for 10 minutes
        time.sleep(60)

        # Move the contents of the destination folder back to the source folder
        while True:
            try:
                shutil.move(dest, src)
                print(f"Moved contents of {dest} to {src}")
                break
            except (PermissionError, OSError) as e:
                print(f"Error: {e}. Waiting for file to be released...")
                time.sleep(1)

    except (PermissionError, OSError) as e:
        print(f"Error: {e}. Waiting for file to be released...")
        time.sleep(1)

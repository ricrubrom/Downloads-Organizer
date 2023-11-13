from os import scandir, remove, rename, makedirs
from os.path import splitext, exists, join, isdir
from shutil import move
from time import sleep
from pathlib import Path
import logging
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

# Define source and destination directories for different file types
source_dir = ""
image_dir = ""
video_dir = ""
audio_dir = ""
document_dir = ""
compressed_dir = ""
executable_dir = ""
game_dir = ""
random_dir = ""

# Supported file extensions for different types
image_extensions = [".jpg", ".jpeg", ".jpe", ".jif", ".jfif", ".jfi", ".png", ".gif", ".webp", ".tiff", ".tif", ".psd", ".raw", ".arw", ".cr2", ".nrw",
                    ".k25", ".bmp", ".dib", ".heif", ".heic", ".ind", ".indd", ".indt", ".jp2", ".j2k", ".jpf", ".jpf", ".jpx", ".jpm", ".mj2", ".svg", ".svgz", ".ai", ".eps", ".ico"]

video_extensions = [".webm", ".mpg", ".mp2", ".mpeg", ".mpe", ".mpv", ".ogg",
                    ".mp4", ".mp4v", ".m4v", ".avi", ".wmv", ".mov", ".qt", ".flv", ".swf", ".avchd"]

audio_extensions = [".m4a", ".flac", "mp3", ".wav", ".wma", ".aac"]

document_extensions = [".doc", ".docx", ".odt",
                        ".pdf", ".xls", ".xlsx", ".ppt", ".pptx"]

compressed_extensions = [".zip", ".rar", ".tar", ".gz", ".bz2", ".7z", ".xz"]

executable_extensions = [".exe", ".msi"]

game_extensions = [".torrent", ".apk"]

def move_file(dest, file, name):
    """
    Move the file to the specified destination directory.
    If a file with the same name exists in the destination, it is removed before moving.

    Parameters:
    - dest (str): Destination directory
    - file (DirEntry): File to be moved
    - name (str): Name of the file
    """
    if exists(f"{dest}/{name}"):
        remove(f"{dest}/{name}")
    move(file, dest)

class MoverHandler(FileSystemEventHandler):
    """
    Custom event handler for file system events.
    """

    def on_modified(self, event):
        """
        Handle the on_modified event triggered by file modifications.
        Move files to their respective directories based on their types.

        Parameters:
        - event (FileSystemEvent): File system event object
        """
        # List of check functions to identify file types
        check_functions = [
            self.check_image,
            self.check_video,
            self.check_audio,
            self.check_document,
            self.check_compressed,
            self.check_executable,
            self.check_game,
        ]

        # Iterate through the files in the source directory
        with scandir(source_dir) as files:
            for file in files:
                name = file.name
                # Iterate through check functions
                for check_function in check_functions:
                    if check_function(file, name):
                        # Exit the loop if any check function returns True
                        break
                else:
                    # This block is executed if none of the check functions return True
                    if not file.is_dir():
                        move_file(random_dir, file, name)

    def check_image(self, file, name):
        """
        Check if the file is an image based on its extension.

        Parameters:
        - file (DirEntry): File to be checked
        - name (str): Name of the file

        Returns:
        - bool: True if the file is an image, False otherwise
        """
        for extension in image_extensions:
            if name.endswith(extension) or name.endswith(extension.upper()):
                dest = image_dir
                move_file(dest, file, name)
                logging.info(f"Moved image file: {name}")
                return True

    def check_video(self, file, name):
        # Check if the file is a video based on its extension
        for extension in video_extensions:
            if name.endswith(extension) or name.endswith(extension.upper()):
                dest = video_dir
                move_file(dest, file, name)
                logging.info(f"Moved video file: {name}")
                return True

    def check_audio(self, file, name):
        # Check if the file is an audio file based on its extension
        for extension in audio_extensions:
            if name.endswith(extension) or name.endswith(extension.upper()):
                dest = audio_dir
                move_file(dest, file, name)
                logging.info(f"Moved audio file: {name}")
                return True

    def check_document(self, file, name):
        # Check if the file is a document based on its extension
        for extension in document_extensions:
            if name.endswith(extension) or name.endswith(extension.upper()):
                dest = document_dir
                move_file(dest, file, name)
                logging.info(f"Moved document file: {name}")
                return True

    def check_compressed(self, file, name):
        # Check if the file is compressed based on its extension
        for extension in compressed_extensions:
            if name.endswith(extension) or name.endswith(extension.upper()):
                dest = compressed_dir
                move_file(dest, file, name)
                logging.info(f"Moved compressed file: {name}")
                return True

    def check_executable(self, file, name):
        # Check if the file is an executable based on its extension
        for extension in executable_extensions:
            if name.endswith(extension) or name.endswith(extension.upper()):
                dest = executable_dir
                move_file(dest, file, name)
                logging.info(f"Moved executable file: {name}")
                return True

    def check_game(self, file, name):
        # Check if the file is a game file based on its extension
        for extension in game_extensions:
            if name.endswith(extension) or name.endswith(extension.upper()):
                dest = game_dir
                move_file(dest, file, name)
                logging.info(f"Moved game file: {name}")
                return True

if __name__ == "__main__":
    # Set up logging
    logging.basicConfig(level=logging.INFO,
                        format='%(asctime)s - %(message)s',
                        datefmt='%Y-%m-%d %H:%M:%S')

    # Set up the observer to monitor file system events
    path = source_dir
    event_handler = MoverHandler()
    observer = Observer()
    observer.schedule(event_handler, path, recursive=False)
    observer.start()

    try:
        # Run an infinite loop to keep the observer running
        while True:
            sleep(10)
    except KeyboardInterrupt:
        # Stop the observer if interrupted by a keyboard interrupt (Ctrl+C)
        observer.stop()
    
    # Wait for the observer to complete its execution
    observer.join()

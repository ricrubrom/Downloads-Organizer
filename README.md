
# File Organizer Script

## Overview

This Python script organizes files in a specified directory based on their types (e.g., images, videos, documents) into designated folders. It uses the watchdog library to monitor file system events.

## Features

- Automatic organization of files into appropriate directories.
- Customizable directories for different file types.
- Runs in the background and can be set to start on Windows startup.

## Prerequisites

- Python installed on your system.
- Required Python packages can be installed using the following:
  ```bash
  pip install watchdog
  ```

## Usage

1. Clone the repository or download the script file.

2. Modify the script to set the source directory and destination directories for different file types.

3. Run the script using the following command:
   ```bash
   python file_organizer.py
   ```

4. The script will run in the background and organize files based on their types.

## Customization

- You can customize the script by adding or modifying the supported file types and their corresponding destination directories.
- Adjust the sleep interval in the script to control how frequently it checks for file modifications.

## Running on Windows Startup

1. Create a shortcut for the script.

2. Press `Win + R` to open the Run dialog.
s
3. Type `shell:startup` and press Enter to open the "Startup" folder.

4. Place the shortcut in the "Startup" folder.

## Author

Romero, Mateo [materomero04@gmail.com](materomero04@gmail.com)

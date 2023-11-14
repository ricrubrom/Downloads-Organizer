
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

2. Customize the script by modifying the `config.json` file to set the source directory and destination directories for different file types. If there are files that you don't want to be moved, you will have to add them to the `blocked_extensions` array in the JSON file.

3. Run the script using the following command:
   ```bash
   python file_organizer.pyw
   ```

4. The script will run in the background and organize files based on their types.

## Customization

- You can customize the script by modifying the `config.json` file to add or modify the supported file types and their corresponding destination directories.
- Adjust the sleep interval in the script to control how frequently it checks for file modifications.

## Running on Windows Startup

1. Create a shortcut for the script.

2. Press `Win + R` to open the Run dialog.

3. Type `shell:startup` and press Enter to open the "Startup" folder.

4. Place the shortcut in the "Startup" folder.

## Author

[Romero, Mateo - materomero04@gmail.com](materomero04@gmail.com)

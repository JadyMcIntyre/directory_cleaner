## Description

The `directory_cleaner` is a Python script that helps organize files in a specified directory by automatically sorting them into folders based on their file extensions. This tool is particularly useful for cleaning up cluttered directories, such as Downloads folders or project directories with mixed file types.

## Features

- Automatically creates folders for each file type encountered
- Moves files into their corresponding folders based on file extension
- Skips hidden files and the script itself to avoid errors
- Provides console output for created folders and moved files

## Requirements

- Python 3.x

## Installation

1. Clone this repository or download the `app.py` file.
2. Ensure you have Python 3.x installed on your system.

## Usage

Run the script from the command line with the following syntax:

For help:
```bash
python app.py -h
```

To clean the directory:
```bash
python app.py --path ./path/to/directory
```

If you want to remove empty folders as well, use the following command:

```bash
python app.py --path ./path/to/directory --remove-empty
```

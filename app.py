# os is used to interact with the operating system
import os
#argparse is used to parse command-line arguments
import argparse

parser = argparse.ArgumentParser(
    description="Clean up a directory by organizing files into subfolders based on their extensions.",
    epilog="Example: python app.py --path /home/user/documents --remove-empty",
    formatter_class=argparse.RawDescriptionHelpFormatter
)

parser.add_argument(
    "--path",
    type=str,
    default=".",
    help="Path of the directory to be cleaned (default: current directory)"
)

parser.add_argument(
    "--remove-empty",
    action="store_true",
    help="Remove empty folders after organizing files"
)

# Parse the arguments given by the user and extract the path
args = parser.parse_args()
path = args.path

# Print the path that will be cleaned
print(f"Cleaning up directory {path}")

# Get all files from the given directory
dir_content = os.listdir(path)

# Create a list of full paths for all items in the directory
path_dir_content = [os.path.join(path, doc) for doc in dir_content]

# Filter directory content into documents and folders list
docs = [doc for doc in path_dir_content if os.path.isfile(doc)]
folders = [folder for folder in path_dir_content if os.path.isdir(folder)]

# Counter to keep track of the number of moved files
moved = 0
# list of already created folders to avoid multiple creations
created_folders = []

# Print the number of files and folders that will be cleaned
print(f"Cleaning up {len(docs)} of {len(dir_content)} elements.")

# Go through all files and move them into corresponding folders
for doc in docs:
    # Separate name from file extension
    full_doc_path, filetype = os.path.splitext(doc)
    doc_path = os.path.dirname(full_doc_path)
    doc_name = os.path.basename(doc)

    # Skip this file when it is the script itself or a hidden file
    if doc_name == os.path.basename(__file__) or doc_name.startswith('.'):
        continue

    # Get the subfolder name and create folder if not exist
    subfolder_path = os.path.join(path, filetype[1:].lower())

    if subfolder_path not in folders and subfolder_path not in created_folders:
        try:
            os.mkdir(subfolder_path)
            created_folders.append(subfolder_path)
            print(f"Folder {subfolder_path} created.")
        except FileExistsError as err:
            print(f"Folder already exists at {subfolder_path}... {err}")

    # Move the file to the new folder
    new_doc_path = os.path.join(subfolder_path, doc_name) + filetype
    os.rename(doc, new_doc_path)
    moved += 1
    print(f"Moved file {doc} to {new_doc_path}")

print(f"Renamed {moved} of {len(docs)} files.")

# Remove empty folders if --remove-empty flag is set
if args.remove_empty:
    empty_folders = []
    for folder in folders:
        if not os.listdir(folder):
            empty_folders.append(folder)
            try:
                os.rmdir(folder)
                print(f"Removed empty folder: {folder}")
            except OSError as e:
                print(f"Error removing folder {folder}: {e}")

    print(f"Removed {len(empty_folders)} empty folders.")

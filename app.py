import os
import argparse

parser = argparse.ArgumentParser(
    description="Clean up directory and put files into corresponding folders based on file extension."
)

parser.add_argument(
    "--path",
    type=str,
    default=".",
    help="Path of the directory to be cleaned",
)

# Parse the arguments given by the user and extract the path
args = parser.parse_args()
path = args.path

print(f"Cleaning up directory {path}")

# Get all files from the given directory
dir_content = os.listdir(path)

# Create a relative path from the path to the file and the document name
path_dir_content = [os.path.join(path, doc) for doc in dir_content]

# Filter directory content into documents and folders list
docs = [doc for doc in path_dir_content if os.path.isfile(doc)]
folders = [folder for folder in path_dir_content if os.path.isdir(folder)]

# Counter to keep track of the number of moved files
# and list of already created folders to avoid multiple creations
moved = 0
created_folders = []

print(f"Cleaning up {len(docs)} of {len(dir_content)} elements.")

# Go through all files and move them into corresponding folders
for doc in docs:
    # Separate name from file extension
    full_doc_path, filetype = os.path.splitext(doc)
    doc_path = os.path.dirname(full_doc_path)
    doc_name = os.path.basename(full_doc_path)

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

import os

def clean_directory(path, remove_empty=False):
    print(f"Cleaning up directory {path}")

    dir_content = os.listdir(path)
    path_dir_content = [os.path.join(path, doc) for doc in dir_content]
    docs = [doc for doc in path_dir_content if os.path.isfile(doc)]
    folders = [folder for folder in path_dir_content if os.path.isdir(folder)]

    moved = 0
    created_folders = []

    print(f"Cleaning up {len(docs)} of {len(dir_content)} elements.")

    for doc in docs:
        full_doc_path, filetype = os.path.splitext(doc)
        doc_name = os.path.basename(full_doc_path)

        if doc_name == os.path.basename(__file__) or doc_name.startswith('.'):
            continue

        subfolder_path = os.path.join(path, filetype[1:].lower())

        if subfolder_path not in folders and subfolder_path not in created_folders:
            try:
                os.mkdir(subfolder_path)
                created_folders.append(subfolder_path)
                print(f"Folder {subfolder_path} created.")
            except FileExistsError as err:
                print(f"Folder already exists at {subfolder_path}... {err}")

        new_doc_path = os.path.join(subfolder_path, doc_name + filetype)
        os.rename(doc, new_doc_path)
        moved += 1
        print(f"Moved file {doc} to {new_doc_path}")

    empty_folders = []
    if remove_empty:
        for folder in folders:
            if not os.listdir(folder):
                empty_folders.append(folder)
                try:
                    os.rmdir(folder)
                    print(f"Removed empty folder: {folder}")
                except OSError as e:
                    print(f"Error removing folder {folder}: {e}")

    return moved, len(docs), len(empty_folders)
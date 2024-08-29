import tkinter as tk
from tkinter import filedialog, messagebox, ttk
from cleaner import clean_directory

def select_directory():
    return filedialog.askdirectory()

def process_cleaning(path, remove_empty):
    if not path:
        messagebox.showerror("Error", "Please select a directory")
        return

    moved, total, empty_removed = clean_directory(path, remove_empty)
    messagebox.showinfo("Cleaning Complete", 
                        f"Moved {moved} of {total} files.\n"
                        f"Removed {empty_removed} empty folders.")

def run_gui():
    root = tk.Tk()
    root.title("Directory Cleaner")
    root.geometry("500x300")
    root.resizable(False, False)

    style = ttk.Style()
    style.theme_use('clam')

    main_frame = ttk.Frame(root, padding="20 20 20 20")
    main_frame.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))

    # Directory Selection Group
    dir_group = ttk.LabelFrame(main_frame, text="Directory Selection", padding="10 10 10 10")
    dir_group.grid(row=0, column=0, columnspan=2, sticky=(tk.W, tk.E), pady=(0, 20))
    dir_group.columnconfigure(0, weight=1)

    path_var = tk.StringVar()
    path_entry = ttk.Entry(dir_group, textvariable=path_var, width=50)
    path_entry.grid(row=0, column=0, sticky=(tk.W, tk.E), padx=(0, 10))

    browse_btn = ttk.Button(dir_group, text="Browse", command=lambda: path_var.set(select_directory()))
    browse_btn.grid(row=0, column=1)

    # Options Group
    options_group = ttk.LabelFrame(main_frame, text="Cleaning Options", padding="10 10 10 10")
    options_group.grid(row=1, column=0, columnspan=2, sticky=(tk.W, tk.E), pady=(0, 20))

    remove_empty_var = tk.BooleanVar()
    remove_empty_cb = ttk.Checkbutton(options_group, text="Remove empty folders", variable=remove_empty_var)
    remove_empty_cb.grid(row=0, column=0, sticky=tk.W)

    # Action Buttons
    clean_btn = ttk.Button(main_frame, text="Clean Directory", 
                           command=lambda: process_cleaning(path_var.get(), remove_empty_var.get()))
    clean_btn.grid(row=2, column=0, sticky=tk.W, pady=(0, 10))

    quit_btn = ttk.Button(main_frame, text="Quit", command=root.quit)
    quit_btn.grid(row=2, column=1, sticky=tk.E, pady=(0, 10))

    # Status Bar
    status_var = tk.StringVar()
    status_var.set("Ready")
    status_bar = ttk.Label(main_frame, textvariable=status_var, relief=tk.SUNKEN, anchor=tk.W)
    status_bar.grid(row=3, column=0, columnspan=2, sticky=(tk.W, tk.E))

    root.mainloop()

if __name__ == "__main__":
    run_gui()
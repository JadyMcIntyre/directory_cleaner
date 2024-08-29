import argparse
from cleaner import clean_directory
from gui import run_gui

def main():
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

    args = parser.parse_args()

    if args.path != ".":
        # Command-line mode
        moved, total, empty_removed = clean_directory(args.path, args.remove_empty)
        print(f"Moved {moved} of {total} files.")
        print(f"Removed {empty_removed} empty folders.")
    else:
        # GUI mode
        run_gui()

if __name__ == "__main__":
    main()

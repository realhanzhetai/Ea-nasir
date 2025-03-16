from pathlib import Path

def get_file_path(filename=None, *subpaths, create_dirs=False):
    root_dir = Path(__file__).parent.absolute()

    target_dir = root_dir / "files"

    # Add any subdirectories specified
    for subpath in subpaths:
        target_dir = target_dir / subpath

    if create_dirs and not target_dir.exists():
        target_dir.mkdir(parents=True, exist_ok=True)

    if filename is None:
        return target_dir

    file_path = target_dir / filename

    if not file_path.exists():
        if create_dirs:
            file_path.parent.mkdir(parents=True, exist_ok=True)
        else:
            raise FileNotFoundError(f"File not found: {file_path}")

    return file_path


# Example usage:
# get_file_path(filename)                           # Original files directory
# get_file_path()                                   # Just get the files directory
# get_file_path(filename, "wiki_supplement")        # Wiki supplement subdirectory
# get_file_path("new_file.txt", create_dirs=True)   # Create directories if needed




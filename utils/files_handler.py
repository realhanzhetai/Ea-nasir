import os

def list_files_in_folder(folder_path):
    try:
        # Check if the folder exists
        if not os.path.isdir(folder_path):
            print(f"Error: '{folder_path}' is not a valid directory")
            return

        # Get list of all files in the folder
        files = os.listdir(folder_path)

        # Print the files
        if files:
            text_for_load = []
            print(f"Files in '{folder_path}':")
            for index, file in enumerate(files, 1):
                # print(f"{index}. {file}")
                text_for_load.append(file)
            return text_for_load
        else:
            print(f"No files found in '{folder_path}'")

    except PermissionError:
        print(f"Error: Permission denied to access '{folder_path}'")
    except Exception as e:
        print(f"Error: {e}")
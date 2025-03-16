import re
import os

def remove_bracketed_numbers(file_path):
    try:
        # Read the file
        with open(file_path, 'r', encoding='utf-8') as file:
            content = file.read()

        # Use regular expression to remove [number] patterns
        modified_content = re.sub(r'\[\d+\]', '', content)

        # Write the modified content back to the file
        with open(file_path, 'w', encoding='utf-8') as file:
            file.write(modified_content)

        print(f"Successfully processed {file_path}")
        print(f"Removed all instances of '[number]' from the text")

    except FileNotFoundError:
        print(f"Error: File '{file_path}' not found")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    # Use absolute path instead
    file_path = r'D:\Dev\pythonProjects\Ea-nasir\files\wiki_supplement_boeing_info'

    # Verify the file exists before processing
    if os.path.exists(file_path):
        remove_bracketed_numbers(file_path)
    else:
        print(f"File not found at: {file_path}")
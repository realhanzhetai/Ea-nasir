import wikipedia
import os
# custom lib
from path_manager import get_file_path

def save_wikipedia_content(topic):
    try:
        # Get Wikipedia content
        print(f"Fetching Wikipedia content for '{topic}'...")
        wiki_page = wikipedia.page(topic)
        content = wiki_page.content

        # Create filename from topic name with no spaces and .txt extension
        filename = f"wiki_supplement_{topic.replace(' ', '_').lower()}_info.txt"
        # Use current directory instead of parent directory
        output_path = get_file_path(filename, 'wiki_supplement', create_dirs=True)

        # Create directory if it doesn't exist
        directory = os.path.dirname(output_path)
        if directory and not os.path.exists(directory):
            try:
                os.makedirs(directory)
                print(f"Created directory: {directory}")
            except PermissionError:
                print(f"Error: No permission to create directory: {directory}")
                # Fall back to current working directory
                filename = os.path.basename(output_path)
                output_path = os.path.join(os.getcwd(), filename)
                print(f"Falling back to current directory: {output_path}")

        # Try to write content to file
        try:
            with open(output_path, "w", encoding="utf-8") as file:
                file.write(content)
            print(f"Content successfully saved to {output_path}")
            return True
        except PermissionError:
            print(f"Error: No permission to write to {output_path}")
            # Try writing to a safe location as a last resort
            safe_path = os.path.join(os.path.expanduser("~"), f"{topic.replace(' ', '_').lower()}_info.txt")
            print(f"Attempting to write to home directory: {safe_path}")
            with open(safe_path, "w", encoding="utf-8") as file:
                file.write(content)
            print(f"Content successfully saved to {safe_path}")
            return True

    except wikipedia.exceptions.PageError:
        print(f"Error: '{topic}' page not found on Wikipedia.")
        return False
    except wikipedia.exceptions.DisambiguationError as e:
        print(f"Error: '{topic}' is ambiguous. Options include: {e.options[:5]}...")
        return False
    except Exception as e:
        print(f"Error: {str(e)}")
        print(f"Error type: {type(e).__name__}")
        return False


if __name__ == "__main__":
    topic = "Economy of the United States"
    success = save_wikipedia_content(topic)

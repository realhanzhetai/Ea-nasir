from lightrag_model_settings import rag

from path_manager import get_file_path

def parse_content(filepath):
    # Read and insert content
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()
            rag.insert(content)
            return content
    except Exception as e:
        raise Exception(f"Error reading file: {e}")


if __name__ == "__main__":
    filename = "wiki_supplement_copper.txt"
    file_path = get_file_path(filename, "wiki_supplement")

    parse_content(file_path)


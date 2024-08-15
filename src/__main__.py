from pathlib import Path
from archive_getter import ArchiveGetter

def main():
    # Define the main directory where the archive will be created
    main_directory = Path("/home/luana/Projects/Python/MarkdownStuff/tests")
    json_path = Path("/home/luana/Projects/Python/MarkdownStuff/src/elements.json")  # Define the path to your JSON file

    # Create an instance of ArchiveGetter
    getter = ArchiveGetter(main_directory, json_path)

    if not getter.dir_path.exists():
        getter.dir_path.mkdir(parents=True)
        getter.create_maindir(main_directory)
        print(f"Directory {getter.dir_path} created.")
    else:
        print(f"Directory {getter.dir_path} already exists.")
    
    # Creating the Pages based on JSON archive
    getter.create_directories_from_json()

    # Use the class to list markdown files in the directory
    markdown_files = getter.return_markdown_files_names()
    
    # Print the list of markdown files
    print("Markdown files found:", markdown_files)

if __name__ == "__main__":
    main()

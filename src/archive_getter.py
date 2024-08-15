import json
import os
from typing import List, Dict
from pathlib import Path
from contextlib import contextmanager

@contextmanager
def chdir(path: Path):
    current_dir = os.getcwd()
    try:
        os.chdir(path)
        yield
    finally:
        os.chdir(current_dir)
        
class ArchiveGetter:
    def __init__(self, dir_path: Path, json_path: Path):
        self.dir_path = dir_path
        self.json_path = json_path
        self.json_data = self.create_json_data()  # Fixed method call

    def check_maindir_exists(self) -> bool:
        return any(self.dir_path.iterdir())

    def create_json_data(self) -> dict:
        try:
            with open(self.json_path, 'r') as file:
                return json.load(file)
        except FileNotFoundError:
            print(f"JSON file not found: {self.json_path}")
            return {}
        except json.JSONDecodeError:
            print(f"Error decoding JSON from file: {self.json_path}")
            return {}
        except Exception as e:
            print(f"An error occurred while reading the JSON file: {e}")
            return {}

    def create_maindir(self, main_dir: Path):
        try:
            if not any(main_dir.iterdir()):
                main_dir.mkdir(parents=True, exist_ok=True)
                main_page_dir = main_dir / "MainPage"
                main_page_dir.mkdir(exist_ok=True)
                with chdir(main_page_dir):
                    with open(self.json_path, 'r') as file:  # Use instance's json_path
                        for item in json.load(file):
                            (main_page_dir / item).mkdir(exist_ok=True)
        except Exception as e:
            print(f"An error occurred while creating the main directory: {e}")
            raise e

    def return_markdown_files_names(self) -> List[str]:
        try:
            return [file.name for file in self.dir_path.iterdir() if file.suffix == ".md"]
        except FileNotFoundError:
            print(f"Directory not found: {self.dir_path}")
            return []
        except Exception as e:
            print(f"An error occurred: {e}")
            return []

    def create_directories_from_json(self):
        def create_subdirectories(base_path: Path, structure: Dict):
            for key, value in structure.items():
                dir_path = base_path / key
                dir_path.mkdir(parents=True, exist_ok=True)
                if isinstance(value, dict):
                    create_subdirectories(dir_path, value)

        try:
            if not self.json_data:
                print("No data to process from JSON.")
                return
            
            create_subdirectories(self.dir_path, self.json_data)
            
        except Exception as e:
            print(f"An error occurred while creating directories from JSON: {e}")
            raise e
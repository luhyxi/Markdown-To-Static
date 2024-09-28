import os
from pathlib import Path
from typing import Dict, List

class MarkdownConverter:

    def __init__(self, dir_path: Path, json_path: Path, md_dict: Dict[str, str]):
        self.dir_path = dir_path
        self.json_path = json_path
        self.md_dict = md_dict

    def get_md_list(self):
        for root, dirs, files in os.walk(self.dir_path):
            for file in files:
                if file.endswith(".md"):
                    file_path = os.path.join(root, file)
                    self.md_dict[file] = file_path

    def turn_md_list_to_page(self):
        for x in self.md_dict:
            return 0
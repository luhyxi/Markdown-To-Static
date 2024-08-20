from pathlib import Path


class markdown_converter:

    def __init__(self, dir_path: Path, json_path: Path):
        self.dir_path = dir_path
        self.json_path = json_path


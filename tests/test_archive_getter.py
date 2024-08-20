import pytest
import json
from pathlib import Path
from tempfile import TemporaryDirectory
from mdstatic import ArchiveGetter 

@pytest.fixture
def temp_dir():
    with TemporaryDirectory() as tmpdirname:
        yield Path(tmpdirname)

@pytest.fixture
def mock_json_file(temp_dir):
    json_path = temp_dir / "test.json"
    data = {"dir1": {}, "dir2": {"subdir1": {}, "subdir2": {}}}
    json_path.write_text(json.dumps(data))
    return json_path

def test_create_maindir(mock_json_file, temp_dir):
    archive_getter = ArchiveGetter(temp_dir, mock_json_file)
    archive_getter.create_maindir(temp_dir / "MainDir")
    assert (temp_dir / "MainDir" / "MainPage" / "dir1").exists()

def test_check_maindir_exists(temp_dir):
    (temp_dir / "file.txt").touch()
    archive_getter = ArchiveGetter(temp_dir, temp_dir / "dummy.json")
    assert archive_getter.check_maindir_exists()

def test_create_json_data(temp_dir):
    archive_getter = ArchiveGetter(temp_dir, temp_dir / "non_existent.json")
    assert archive_getter.json_data == {}


def test_create_directories_from_json(mock_json_file, temp_dir):
    archive_getter = ArchiveGetter(temp_dir, mock_json_file)
    archive_getter.create_directories_from_json()
    assert (temp_dir / "dir2" / "subdir2").exists()

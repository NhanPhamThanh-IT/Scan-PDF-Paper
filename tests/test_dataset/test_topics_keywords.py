"""
Test suite for verifying the structure and integrity of keyword topic JSON files.

This module ensures that all `.json` files under the `topics_keywords` directory:
    - Exist and are not empty.
    - Contain valid JSON data.
    - Store a list of lowercase strings without duplicates.
    - Follow filename naming conventions (capitalized first letter).

Dependencies:
    - pytest: For running tests and parametrizing file checks.
    - json: For parsing JSON files.
    - os: For file system access.
"""

import os
import json
import pytest

# Constants
PROJECT_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))
DATA_DIR = os.path.join(PROJECT_ROOT, "app", "data", "topics_keywords")
FILE_EXT = ".json"

# Helpers

def get_json_files():
    """
    Lists all `.json` files in the `topics_keywords` data directory.

    Returns:
        list[str]: A list of filenames with `.json` extension.
    """
    return [
        f for f in os.listdir(DATA_DIR)
        if f.endswith(FILE_EXT) and os.path.isfile(os.path.join(DATA_DIR, f))
    ]

def read_json_file(filename):
    """
    Reads and parses a JSON file from the data directory.

    Args:
        filename (str): Name of the JSON file to read.

    Returns:
        Any: Parsed Python object from the JSON content.
    """
    with open(os.path.join(DATA_DIR, filename), "r", encoding="utf-8") as f:
        return json.load(f)

# Tests

def test_topics_keywords_folder_exists():
    """
    Tests that the `topics_keywords` folder exists.
    """
    assert os.path.isdir(DATA_DIR), f"Folder not found: {DATA_DIR}"

@pytest.mark.parametrize("filename", get_json_files())
def test_file_is_not_empty(filename):
    """
    Tests that each JSON file is not empty.

    Args:
        filename (str): The name of the JSON file.
    """
    content = open(os.path.join(DATA_DIR, filename), "r", encoding="utf-8").read()
    assert content.strip(), f"{filename} is empty"

@pytest.mark.parametrize("filename", get_json_files())
def test_file_is_valid_json(filename):
    """
    Tests that each JSON file contains valid JSON content.

    Args:
        filename (str): The name of the JSON file.
    """
    try:
        read_json_file(filename)
    except json.JSONDecodeError as e:
        pytest.fail(f"{filename} is not valid JSON: {e}")

@pytest.mark.parametrize("filename", get_json_files())
def test_file_is_list(filename):
    """
    Tests that the JSON data is a list.

    Args:
        filename (str): The name of the JSON file.
    """
    data = read_json_file(filename)
    assert isinstance(data, list), f"{filename} does not contain a list"

@pytest.mark.parametrize("filename", get_json_files())
def test_list_is_not_empty(filename):
    """
    Tests that the list in each JSON file is not empty.

    Args:
        filename (str): The name of the JSON file.
    """
    data = read_json_file(filename)
    assert data, f"{filename} contains an empty list"

@pytest.mark.parametrize("filename", get_json_files())
def test_list_has_no_duplicates(filename):
    """
    Tests that the list in each JSON file contains no duplicate values.

    Args:
        filename (str): The name of the JSON file.
    """
    data = read_json_file(filename)
    assert len(data) == len(set(data)), f"{filename} contains duplicate entries"

@pytest.mark.parametrize("filename", get_json_files())
def test_filename_is_capitalized(filename):
    """
    Tests that the filename starts with a capital letter.

    Args:
        filename (str): The name of the JSON file.
    """
    assert filename[0].isupper(), f"{filename} is not capitalized"

@pytest.mark.parametrize("filename", get_json_files())
def test_all_values_are_lowercase(filename):
    """
    Tests that all items in the JSON list are lowercase strings.

    Args:
        filename (str): The name of the JSON file.
    """
    data = read_json_file(filename)
    for item in data:
        assert isinstance(item, str) and item.islower(), \
            f"{filename} contains non-lowercase value: {item}"

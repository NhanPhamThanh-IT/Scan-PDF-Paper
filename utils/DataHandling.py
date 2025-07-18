"""
DataHandling.py

This module provides functionality to load all local topic-related JSON files
from a given directory into a structured dictionary.

Features:
    - Automatically detects all `.json` files in the specified folder.
    - Uses the FileHandling module to read each JSON file.
    - Returns a dictionary where each key is the file name and the value is the parsed content.

Requirements:
    - JSON files must be valid and located in the given folder.
    - The FileHandling module must expose a `load_data_from_json(path: str) -> Dict[str, Any]` function.

Author: Nhan Pham
Created: 2025-07-18
"""

import os
from typing import Any, Dict
from .FileHandling import FileHandling

class DataHandling:
    """
    A utility class for handling the loading of local topic JSON files.
    """

    @staticmethod
    def load_local_topics_data(folder_path: str) -> Dict[str, Dict[str, Any]]:
        """
        Load all JSON topic files from a given folder into a dictionary.

        Args:
            folder_path (str): Path to the folder containing JSON files.

        Returns:
            Dict[str, Dict[str, Any]]: A dictionary where:
                - keys are filenames (including the '.json' extension)
                - values are dictionaries representing the JSON content of each file.
        """
        return {
            filename: FileHandling.load_data_from_json(os.path.join(folder_path, filename))
            for filename in os.listdir(folder_path)
            if filename.endswith(".json")
        }

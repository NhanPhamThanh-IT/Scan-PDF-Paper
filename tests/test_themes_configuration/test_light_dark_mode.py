"""
Test suite for validating consistency and integrity of CSS theme files across light and dark modes.

This module ensures that:
- Each theme folder exists and contains valid CSS files.
- All CSS files are non-empty.
- The filenames and structure of both light and dark theme folders are consistent.
- CSS selectors defined in each theme are symmetrical and complete.

Dependencies:
- pytest: for running parameterized tests
- tinycss2: for parsing CSS and extracting selectors
"""

import os
import pytest
import tinycss2

# Constants
PROJECT_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))
THEME_DIR = os.path.join(PROJECT_ROOT, "app", "assets", "themes")
THEMES = ["light_mode", "dark_mode"]

# Utility functions

def get_theme_path(theme):
    """
    Construct the absolute path to a theme directory.

    Args:
        theme (str): The name of the theme (e.g., "light_mode").

    Returns:
        str: Absolute path to the theme folder.
    """
    return os.path.join(THEME_DIR, theme)

def list_css_files(theme_path):
    """
    List all CSS file paths in a given theme directory.

    Args:
        theme_path (str): Path to the theme folder.

    Returns:
        List[str]: Sorted list of absolute CSS file paths.
    """
    return sorted([
        os.path.join(theme_path, file)
        for file in os.listdir(theme_path)
        if file.endswith(".css") and os.path.isfile(os.path.join(theme_path, file))
    ])

def read_file(path):
    """
    Read the content of a file and return it as a stripped string.

    Args:
        path (str): Path to the file.

    Returns:
        str: File content with whitespace trimmed.
    """
    with open(path, encoding="utf-8") as f:
        return f.read().strip()

def extract_selectors(css_content):
    """
    Extract individual CSS selectors from a block of CSS content.

    Args:
        css_content (str): Raw CSS content.

    Returns:
        Set[str]: A set of unique CSS selectors found in the content.
    """
    rules = tinycss2.parse_stylesheet(css_content, skip_comments=True, skip_whitespace=True)
    selectors = set()
    for rule in rules:
        if rule.type == "qualified-rule":
            raw = tinycss2.serialize(rule.prelude).strip()
            selectors.update(s.strip() for s in raw.split(","))
    return selectors

def extract_theme_selectors(theme):
    """
    Extract all CSS selectors from all CSS files in a theme.

    Args:
        theme (str): Theme name (e.g., "dark_mode").

    Returns:
        Set[str]: All CSS selectors used across the theme.
    """
    theme_path = get_theme_path(theme)
    selectors = set()
    for file in list_css_files(theme_path):
        content = read_file(file)
        selectors |= extract_selectors(content)
    return selectors

# Test cases

@pytest.mark.parametrize("theme", THEMES)
def test_theme_folder_exists(theme):
    """
    Ensure the theme folder exists.

    Args:
        theme (str): Name of the theme folder.

    Raises:
        AssertionError: If the folder does not exist.
    """
    assert os.path.isdir(get_theme_path(theme)), f"{theme} folder does not exist"

@pytest.mark.parametrize("theme", THEMES)
def test_css_files_not_empty(theme):
    """
    Ensure all CSS files in a theme folder are not empty.

    Args:
        theme (str): Name of the theme folder.

    Raises:
        AssertionError: If any CSS file is empty or no CSS files exist.
    """
    css_files = list_css_files(get_theme_path(theme))
    assert css_files, f"No CSS files in {theme}"
    for file in css_files:
        assert read_file(file), f"{file} is empty"

def test_same_css_file_names():
    """
    Verify that light and dark mode themes have the same set of CSS filenames.

    Raises:
        AssertionError: If file lists differ between themes.
    """
    light = [os.path.basename(f) for f in list_css_files(get_theme_path("light_mode"))]
    dark = [os.path.basename(f) for f in list_css_files(get_theme_path("dark_mode"))]
    assert light == dark, f"CSS file mismatch\nLight: {light}\nDark: {dark}"

def test_same_selectors_across_themes():
    """
    Ensure both light and dark mode themes define the same set of CSS selectors.

    Raises:
        AssertionError: If any selector exists in one theme but not the other.
    """
    light_selectors = extract_theme_selectors("light_mode")
    dark_selectors = extract_theme_selectors("dark_mode")

    missing_in_dark = light_selectors - dark_selectors
    missing_in_light = dark_selectors - light_selectors

    assert not missing_in_dark and not missing_in_light, (
        "Selector mismatch between themes\n"
        f"Missing in dark: {sorted(missing_in_dark)}\n"
        f"Missing in light: {sorted(missing_in_light)}"
    )

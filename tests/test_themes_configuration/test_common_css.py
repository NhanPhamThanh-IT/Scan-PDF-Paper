"""
Unit tests for validating the presence and content of the shared `common.css` file.

This module verifies:
- That the `common.css` file exists within the expected theme directory.
- That the file is not empty, ensuring it contains usable CSS definitions.

Fixtures:
    load_css (pytest fixture): A utility function that loads CSS content from a relative path.
"""

def test_common_css_exists(load_css):
    """
    Ensure the `common.css` file exists in the themes directory.

    Args:
        load_css (Callable[[str], str]): Pytest fixture to load CSS content by relative path.

    Raises:
        AssertionError: If the file is missing or could not be read.
    """
    content = load_css("assets/themes/common.css")
    assert content is not None, "CSS file not found"

def test_common_css_not_empty(load_css):
    """
    Ensure the `common.css` file is not empty.

    Args:
        load_css (Callable[[str], str]): Pytest fixture to load CSS content by relative path.

    Raises:
        AssertionError: If the file exists but contains no content.
    """
    content = load_css("assets/themes/common.css")
    assert content.strip() != "", "CSS file is empty"

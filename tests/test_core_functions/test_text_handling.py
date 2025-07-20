"""
Test suite for the `calculate_topic_match` method in the TextHandling module.

This module verifies the correctness and robustness of the keyword matching logic
by testing various input cases. The method under test computes the percentage of
matched keywords in a given text, along with the number of keyword hits and the
total number of words.

Test cases include:
    - Matching multiple keywords in the text.
    - Text with no matching keywords.
    - Empty input text.
    - Empty keyword list.
    - Case-insensitive keyword matching.

Dependencies:
    - pytest: For parameterized testing.
    - app.core.TextHandling: Contains the implementation of the `calculate_topic_match` method.
"""

import pytest
from core.TextHandling import TextHandling

@pytest.mark.parametrize(
    "text, keywords, expected_keyword_count, expected_total_words, expected_percent",
    [
        # Case 1: Matching 3 keywords
        (
            "A clean and green environment is very important.",
            ["environment", "clean", "green"],
            3, 8, round((3 / 8) * 100, 3)
        ),
        # Case 2: No keyword matches
        (
            "This sentence contains no relevant terms.",
            ["climate", "energy"],
            0, 6, 0
        ),
        # Case 3: Empty input text
        (
            "",
            ["protection", "environment"],
            0, 0, 0
        ),
        # Case 4: Empty keywords list
        (
            "We must act now to protect the environment.",
            [],
            0, 8, 0
        ),
        # Case 5: Case insensitivity check
        (
            "RENEWABLE energy supports a healthy ENVIRONMENT.",
            ["renewable energy", "environment"],
            2, 6, round((2 / 6) * 100, 3)
        ),
    ]
)
def test_calculate_topic_match(text, keywords, expected_keyword_count, expected_total_words, expected_percent):
    """
    Tests the `calculate_topic_match` function with various inputs.

    Verifies that the function correctly:
        - Counts how many keywords appear in the input text.
        - Computes the total number of words in the text.
        - Calculates the keyword match percentage.

    Args:
        text (str): Input text to be analyzed.
        keywords (list[str]): List of keywords to match against the text.
        expected_keyword_count (int): Expected number of matched keywords in the text.
        expected_total_words (int): Expected total word count in the input text.
        expected_percent (float): Expected match percentage (rounded to 3 decimal places).
    """
    match_percent, keyword_count, total_words = TextHandling.calculate_topic_match(text, keywords)

    assert keyword_count == expected_keyword_count
    assert total_words == expected_total_words
    assert round(match_percent, 3) == expected_percent

"""
Unit test suite for validating the functionality of ResultItem and ResultComponent classes
from the `ui.ResultComponent` module.

These tests ensure:
    - Proper label formatting and value display in ResultItem.
    - Correct instantiation and parsing behavior in ResultComponent.
    - Safe handling of edge cases like None, nested types, and invalid input types.
    - HTML generation by _styled_card() includes expected structure.
    - Streamlit rendering functions (markdown, columns) are called correctly using mocks.

Tools:
    - pytest
    - pytest-mock (for mocking Streamlit methods)

Author: Nhan Pham
Date: 2025-07-20
"""

import pytest
from ui.ResultComponent import ResultItem, ResultComponent

# =======================
# ResultItem Unit Tests
# =======================

@pytest.mark.parametrize(
    "key, expected_label",
    [
        ("match_score", "Match Score"),
        ("accuracy_percent", "Accuracy Percent"),
        ("user_input_count", "User Input Count"),
        ("simple", "Simple"),
        ("", ""),
    ]
)
def test_result_item_label(key, expected_label):
    """
    Test that ResultItem.label formats the key correctly:
    - Replaces underscores with spaces.
    - Capitalizes each word.
    """
    item = ResultItem(key, 1)
    assert item.label == expected_label


@pytest.mark.parametrize(
    "key, value, expected_value",
    [
        ("match_score", 88, "88%"),
        ("accuracy_percent", 95.5, "95.5%"),
        ("partial_match_rate", 62, "62%"),
        ("percentile_rank", "85%", "85%"),
        ("raw_score", 42, "42"),
        ("description", "Excellent", "Excellent"),
        ("level", 3.1415, "3.1415"),
        ("percentage", 100, "100%"),
        ("matchScore", 70, "70%"),
        ("perfect_match_ratio", 1.0, "1.0%"),
    ]
)
def test_result_item_formatted_value(key, value, expected_value):
    """
    Test that ResultItem.formatted_value:
    - Appends '%' if key indicates a percentage or match metric.
    - Returns string representation otherwise.
    """
    item = ResultItem(key, value)
    assert item.formatted_value == expected_value


def test_result_item_with_none_key_should_raise():
    """
    Ensure ResultItem raises TypeError when key is not a string.
    """
    with pytest.raises(TypeError):
        ResultItem(None, 100)


def test_result_item_with_invalid_object_value():
    """
    Ensure ResultItem accepts non-primitive types and formats them as strings.
    """
    class Dummy:
        def __str__(self):
            return "DummyObject"

    item = ResultItem("object_val", Dummy())
    assert isinstance(item.formatted_value, str)
    assert "DummyObject" in item.formatted_value

# ============================
# ResultComponent Unit Tests
# ============================

def test_result_component_parsing():
    """
    Test that ResultComponent correctly parses a valid dict into ResultItem list.
    """
    data = {
        "match_score": 88,
        "description": "Good",
        "total_words": 120,
    }
    component = ResultComponent(data)
    assert len(component.result_items) == 3
    assert [item.key for item in component.result_items] == list(data.keys())


def test_result_component_empty_input():
    """
    Ensure empty input dictionary results in an empty result_items list.
    """
    component = ResultComponent({})
    assert component.result_items == []


def test_result_component_with_none_dict_should_fail():
    """
    Ensure passing None as input raises a TypeError.
    """
    with pytest.raises(TypeError):
        ResultComponent(None)


def test_result_component_with_non_dict_input():
    """
    Ensure that non-dictionary input (e.g., list) raises TypeError.
    """
    with pytest.raises(TypeError):
        ResultComponent(["invalid", "input"])


def test_result_component_with_mixed_types():
    """
    Validate component behavior when input dictionary contains diverse value types,
    including None, list, dict, int, and str.
    """
    data = {
        "score": 95,
        "comment": "Good",
        "bonus": None,
        "nested": {"a": 1},
        "list_value": [1, 2, 3],
    }
    component = ResultComponent(data)
    assert len(component.result_items) == 5

    for item in component.result_items:
        assert isinstance(item.label, str)
        assert isinstance(item.formatted_value, str)


def test_result_component_with_empty_string_key():
    """
    Ensure keys that are empty strings are accepted and handled gracefully.
    """
    data = {"": 123}
    component = ResultComponent(data)
    assert component.result_items[0].label == ""
    assert component.result_items[0].formatted_value == "123"

# ================================
# _styled_card() HTML Output Test
# ================================

@pytest.mark.parametrize(
    "label, value",
    [
        ("Accuracy", "95%"),
        ("Score", "100"),
        ("Performance", "Excellent"),
        ("", ""),
    ]
)
def test_styled_card_html_contains_content(label, value):
    """
    Validate that the HTML returned by _styled_card contains:
    - The provided label and value
    - Basic structural tags and inline styles
    """
    html = ResultComponent._styled_card(label, value)
    assert label in html
    assert value in html
    assert "<div" in html
    assert "background-color" in html

# ================================
# Streamlit Integration Rendering
# ================================

def test_render_streamlit_calls(mocker):
    """
    Test that render() method in ResultComponent:
    - Calls Streamlit's markdown and columns correctly
    - Works with two result items
    """
    import streamlit as st
    mock_markdown = mocker.patch.object(st, "markdown")
    mock_columns = mocker.patch.object(st, "columns", return_value=[mocker.Mock(), mocker.Mock()])

    ResultComponent({"match_score": 90, "status": "OK"}).render()

    assert mock_markdown.called
    assert mock_columns.called
    assert mock_columns.call_args[0][0] == 2


def test_render_with_one_column(mocker):
    """
    Validate render behavior when there is only one result item (1 column).
    """
    import streamlit as st
    mock_markdown = mocker.patch.object(st, "markdown")
    mock_columns = mocker.patch.object(st, "columns", return_value=[mocker.Mock()])

    ResultComponent({"only_one": 1}).render()

    assert mock_columns.called
    assert mock_columns.call_args[0][0] == 1

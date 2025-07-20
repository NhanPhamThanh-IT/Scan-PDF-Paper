"""
UI component for displaying analysis results in a Streamlit application.

This module defines a `ResultItem` dataclass to represent individual result entries,
and a `ResultComponent` class to render those entries in a responsive, styled layout
using Streamlit.

Classes:
    - ResultItem: Encapsulates a single result with formatted display properties.
    - ResultComponent: Renders a list of result items as HTML-styled cards.

Requirements:
    - Streamlit must be installed.
    - Input must be a dictionary of key-value pairs (str, int, or float).

Author: Nhan Pham
Date: 2025-07-18
"""

import streamlit as st
from dataclasses import dataclass
from typing import List, Union, Dict


@dataclass
class ResultItem:
    """
    Represents a single key-value pair in the analysis results.

    Attributes:
        key (str): Identifier of the result metric.
        value (Union[str, int, float]): Value associated with the result.
    """

    key: str
    value: Union[str, int, float]

    def __post_init__(self):
        """
        Validates that the key is a string.

        Raises:
            TypeError: If the key is not a string.
        """
        if not isinstance(self.key, str):
            raise TypeError("key must be a string")

    @property
    def label(self) -> str:
        """
        Returns a human-friendly version of the key.

        Replaces underscores with spaces and capitalizes each word.

        Returns:
            str: Formatted label.
        """
        return self.key.replace("_", " ").title()

    @property
    def formatted_value(self) -> str:
        """
        Returns a display-friendly version of the value.

        If the key suggests a percentage (e.g., contains "percent" or "match"),
        appends a '%' symbol.

        Returns:
            str: Formatted value as a string.
        """
        if any(kw in self.key.lower() for kw in ["percent", "match"]):
            return f"{self.value}%" if isinstance(self.value, (int, float)) else str(self.value)
        return str(self.value)


class ResultComponent:
    """
    Renders analysis results as styled cards in a Streamlit layout.

    Attributes:
        result_items (List[ResultItem]): Parsed result entries to display.
    """

    def __init__(self, analysis_result: Dict[str, Union[str, int, float]]):
        """
        Initializes the result component with a dictionary of results.

        Args:
            analysis_result (dict): Key-value pairs representing analysis metrics.

        Raises:
            TypeError: If input is not a dictionary.
        """
        if not isinstance(analysis_result, dict):
            raise TypeError("analysis_result must be a dictionary")

        self.result_items: List[ResultItem] = [
            ResultItem(key, value) for key, value in analysis_result.items()
        ]

    def render(self) -> None:
        """
        Displays all result items as styled cards in Streamlit columns.
        """
        st.markdown("<h3 style='text-align: center;'>Analysis Result</h3>", unsafe_allow_html=True)
        cols = st.columns(len(self.result_items))

        for col, item in zip(cols, self.result_items):
            col.markdown(self._styled_card(item.label, item.formatted_value), unsafe_allow_html=True)

    @staticmethod
    def _styled_card(label: str, value: str) -> str:
        """
        Builds an HTML snippet for displaying a result card.

        Args:
            label (str): The result's label.
            value (str): The formatted value.

        Returns:
            str: HTML block for rendering the card.
        """
        return f"""
            <div style='text-align: center; padding: 10px; border: 1px solid #ddd;
                        border-radius: 10px; background-color: #f9f9f9;'>
                <div style='font-size: 16px; color: #555;'>{label}</div>
                <div style='font-size: 22px; font-weight: bold; color: #222;'>{value}</div>
            </div>
        """

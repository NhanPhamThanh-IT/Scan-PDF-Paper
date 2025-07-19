"""
ResultComponent.py

This module defines UI components and data structures for rendering analysis results
in a clean and responsive layout using Streamlit.

Features:
    - Defines a ResultItem dataclass to encapsulate individual result entries.
    - Formats result labels and values for improved readability and clarity.
    - Renders result items as styled HTML cards displayed in columns.

Requirements:
    - Streamlit must be installed and configured in the environment.
    - Input data should be a dictionary of key-value pairs, where values are strings,
      integers, or floats.

Author: Nhan Pham
Date: 2025-07-18
"""

import streamlit as st
from dataclasses import dataclass
from typing import List, Union, Dict


@dataclass
class ResultItem:
    """
    Represents a single analysis result item.

    Attributes:
        key (str): The name or identifier of the result.
        value (Union[str, int, float]): The associated value of the result.
    """

    key: str
    value: Union[str, int, float]

    @property
    def label(self) -> str:
        """
        Returns a display-friendly version of the key.

        Replaces underscores with spaces and capitalizes words.

        Returns:
            str: Formatted label.
        """
        return self.key.replace("_", " ").title()

    @property
    def formatted_value(self) -> str:
        """
        Returns a display-friendly version of the value.

        Adds a '%' suffix if the key indicates a percentage or match metric.

        Returns:
            str: Formatted value as a string.
        """
        if any(kw in self.key.lower() for kw in ["percent", "match"]):
            return f"{self.value}%" if isinstance(self.value, (int, float)) else str(self.value)
        return str(self.value)


class ResultComponent:
    """
    A component class that renders analysis results using styled Streamlit components.

    Attributes:
        result_items (List[ResultItem]): Parsed list of result items to be displayed.
    """

    def __init__(self, analysis_result: Dict[str, Union[str, int, float]]):
        """
        Initializes the ResultComponent with analysis result data.

        Args:
            analysis_result (Dict[str, Union[str, int, float]]): Dictionary of analysis results.
        """
        self.result_items: List[ResultItem] = [
            ResultItem(key, value) for key, value in analysis_result.items()
        ]

    def render(self) -> None:
        """
        Renders result items as styled cards in columns within the Streamlit app.
        """
        st.markdown("<h3 style='text-align: center;'>Analysis Result</h3>", unsafe_allow_html=True)
        cols = st.columns(len(self.result_items))

        for col, item in zip(cols, self.result_items):
            col.markdown(self._styled_card(item.label, item.formatted_value), unsafe_allow_html=True)

    @staticmethod
    def _styled_card(label: str, value: str) -> str:
        """
        Generates a styled HTML snippet for a single result card.

        Args:
            label (str): The title or label of the result.
            value (str): The formatted value to display.

        Returns:
            str: An HTML block for rendering the result card.
        """
        return f"""
            <div style='text-align: center; padding: 10px; border: 1px solid #ddd;
                        border-radius: 10px; background-color: #f9f9f9;'>
                <div style='font-size: 16px; color: #555;'>{label}</div>
                <div style='font-size: 22px; font-weight: bold; color: #222;'>{value}</div>
            </div>
        """

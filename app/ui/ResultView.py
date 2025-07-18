"""
ResultView module for rendering analysis results in a Streamlit app.

This module defines data structures and UI logic to present analysis results
in a user-friendly, styled format using the Streamlit library.
"""

import streamlit as st
from dataclasses import dataclass
from typing import List, Union, Dict


@dataclass
class ResultItem:
    """
    Represents a single result item with a key and its associated value.

    Attributes:
        key (str): The identifier or name of the result.
        value (Union[str, int, float]): The actual result value.
    """

    key: str
    value: Union[str, int, float]

    @property
    def label(self) -> str:
        """
        Returns a formatted label for display purposes.

        Returns:
            str: The key converted to title case with underscores replaced by spaces.
        """
        return self.key.replace("_", " ").title()

    @property
    def formatted_value(self) -> str:
        """
        Returns the value formatted as a string. Adds a '%' symbol for keys containing
        'percent' or 'match'.

        Returns:
            str: Formatted result value as string.
        """
        if any(kw in self.key.lower() for kw in ["percent", "match"]):
            return f"{self.value}%" if isinstance(self.value, (int, float)) else str(self.value)
        return str(self.value)


class ResultView:
    """
    A view class that renders a list of analysis results using Streamlit components.

    Attributes:
        result_items (List[ResultItem]): A list of parsed result items for display.
    """

    def __init__(self, analysis_result: Dict[str, Union[str, int, float]]):
        """
        Initializes the ResultView with a dictionary of analysis results.

        Args:
            analysis_result (Dict[str, Union[str, int, float]]): A dictionary containing result data.
        """
        self.result_items: List[ResultItem] = [
            ResultItem(key, value) for key, value in analysis_result.items()
        ]

    def render(self) -> None:
        """
        Renders the result items as styled cards arranged in columns in the Streamlit app.
        """
        st.markdown("<h3 style='text-align: center;'>Analysis Result</h3>", unsafe_allow_html=True)
        cols = st.columns(len(self.result_items))

        for col, item in zip(cols, self.result_items):
            col.markdown(self._styled_card(item.label, item.formatted_value), unsafe_allow_html=True)

    @staticmethod
    def _styled_card(label: str, value: str) -> str:
        """
        Generates a styled HTML card to display a result item.

        Args:
            label (str): The label to be shown as the title.
            value (str): The value to be displayed.

        Returns:
            str: An HTML string for rendering a result card.
        """
        return f"""
            <div style='text-align: center; padding: 10px; border: 1px solid #ddd; border-radius: 10px; background-color: #f9f9f9;'>
                <div style='font-size: 16px; color: #555;'>{label}</div>
                <div style='font-size: 22px; font-weight: bold; color: #222;'>{value}</div>
            </div>
        """

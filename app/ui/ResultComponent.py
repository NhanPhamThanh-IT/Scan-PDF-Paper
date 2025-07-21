"""
UI component for displaying analysis results in a Streamlit application.

Defines:
    - ResultItem: Represents an individual key-value pair.
    - ResultComponent: Displays a list of result items as styled cards.

Requirements:
    - Streamlit must be installed.
    - Input must be a dictionary of (str, int, float, or str) values.

Author: Nhan Pham
Date: 2025-07-18
"""

import streamlit as st
from dataclasses import dataclass
from typing import List, Union, Dict
import math


@dataclass
class ResultItem:
    """Represents a single key-value pair in the analysis results."""
    key: str
    value: Union[str, int, float]

    def __post_init__(self):
        if not isinstance(self.key, str):
            raise TypeError("Key must be a string.")

    @property
    def label(self) -> str:
        """Converts snake_case to Title Case."""
        return self.key.replace("_", " ").title()

    @property
    def formatted_value(self) -> str:
        """Formats value, appending '%' for percent/match-related keys."""
        if any(k in self.key.lower() for k in ("percent", "match")) and isinstance(self.value, (int, float)):
            return f"{self.value}%"
        return str(self.value)


class ResultComponent:
    """Displays analysis results in responsive Streamlit cards."""

    def __init__(
        self,
        title: str,
        analysis_result: Dict[str, Union[str, int, float]],
        cards_per_row: int = 3,
        card_style: Dict[str, str] = None,
        title_style: str = "text-align: center"
    ):
        if not isinstance(analysis_result, dict):
            raise TypeError("analysis_result must be a dictionary.")

        self.title = title
        self.cards_per_row = cards_per_row
        self.title_style = title_style
        self.result_items: List[ResultItem] = [
            ResultItem(k, v) for k, v in analysis_result.items()
        ]

        self.card_style = card_style or {
            "container": "text-align: center; padding: 10px; border-radius: 10px; background-color: #f5f6fa;",
            "label": "font-size: 16px; color: #555;",
            "value": "font-size: 22px; font-weight: bold; color: #222;",
        }

    def render(self) -> None:
        """Renders the result items as cards in a responsive grid."""
        st.markdown(f"<h3 style='{self.title_style}'>{self.title}</h3>", unsafe_allow_html=True)

        num_rows = math.ceil(len(self.result_items) / self.cards_per_row)

        for row in range(num_rows):
            start = row * self.cards_per_row
            end = start + self.cards_per_row
            row_items = self.result_items[start:end]
            cols = st.columns(len(row_items))

            for col, item in zip(cols, row_items):
                col.markdown(self._render_card(item), unsafe_allow_html=True)

    def _render_card(self, item: ResultItem) -> str:
        """Renders a single card using inline HTML and provided styles."""
        return f"""
            <div style="{self.card_style['container']}">
                <div style="{self.card_style['label']}">{item.label}</div>
                <div style="{self.card_style['value']}">{item.formatted_value}</div>
            </div>
        """

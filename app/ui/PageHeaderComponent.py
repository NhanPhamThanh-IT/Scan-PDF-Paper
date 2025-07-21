"""
UI component for displaying a page header in a Streamlit application.

Defines:
    - PageHeaderComponent: Displays a page title and optional subtitle with styled headings.

Requirements:
    - Streamlit must be installed.
    - Input must be strings (title is required, subtitle is optional).

Author: Nhan Pham  
Date: 2025-07-21
"""

import streamlit as st

class PageHeaderComponent:
    """Displays a page header with a centered title and optional subtitle."""

    def __init__(self, title: str, subtitle: str = None):
        """
        Initializes the PageHeaderComponent with a main title and optional subtitle.

        Args:
            title (str): The primary title text displayed as a level-1 header.
            subtitle (str, optional): An optional subtitle displayed as a level-2 header below the title.
        """
        self.title = title
        self.subtitle = subtitle

    def render(self) -> None:
        """
        Renders the header section using Streamlit with HTML styling.

        The title is displayed as an H1 heading, and if a subtitle is provided,
        it is rendered as an H2 heading. Both elements are center-aligned using inline HTML.
        """
        if self.title:
            st.markdown(f"<h2 style='text-align: center;'>{self.title}</h2>", unsafe_allow_html=True)
        if self.subtitle:
            st.markdown(f"<p style='text-align: center;'>{self.subtitle}</p>", unsafe_allow_html=True)

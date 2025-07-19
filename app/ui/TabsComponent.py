import streamlit as st
from dataclasses import dataclass
from typing import List, Callable, Dict, Any


@dataclass
class TabConfig:
    title: str
    render_function: Callable[[], None]

    @staticmethod
    def from_dict(data: Dict[str, Any]) -> 'TabConfig':
        """
        Create a TabConfig instance from a dictionary.

        Args:
            data (dict): Dictionary with keys "title" and "render_function".

        Returns:
            TabConfig: A configured instance.
        """
        return TabConfig(
            title=data["title"],
            render_function=data["render_function"]
        )


class TabsComponent:
    def __init__(self, tabs_config: List[Dict[str, Any]]):
        """
        Initialize with a list of tab config dictionaries.

        Args:
            tabs_config (List[Dict]): Each dict should contain:
                - "title": str
                - "render_function": Callable[[], None]

        Returns:
            None
        """
        self.tabs_config = [TabConfig.from_dict(cfg) for cfg in tabs_config]

    def render(self) -> None:
        """
        Render the tabs based on provided configuration.
        
        Args:
            None
        
        Returns:
            None
        """
        tab_titles = [tab.title for tab in self.tabs_config]
        tab_objects = st.tabs(tab_titles)

        for tab, config in zip(tab_objects, self.tabs_config):
            with tab:
                config.render_function()

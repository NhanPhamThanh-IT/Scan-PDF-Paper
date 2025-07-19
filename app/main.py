import os
import sys
import streamlit as st

# Add current directory to sys.path for module resolution
BASE_DIR = os.path.dirname(__file__)
sys.path.append(BASE_DIR)

# Local imports
from ui import TabsComponent
from views import MainView, SettingsView, HelpsView

def run_app():
    st.markdown(
        "<h1 style='text-align: center;'>PDF Topic Analyzer</h1>",
        unsafe_allow_html=True
    )

    TabsComponent([
        {
            "title": "Home",
            "render_function": MainView.render
        },
        {
            "title": "Settings",
            "render_function": SettingsView.render
        },
        {
            "title": "Helps",
            "render_function": HelpsView.render
        },
    ]).render()

if __name__ == "__main__":
    run_app()

import streamlit as st
import os

class ThemeManager:
    BASE_DIR = os.path.dirname(os.path.abspath(__file__))

    @staticmethod
    def apply():
        current_theme = st.session_state.get("dark_mode", False)
        ThemeManager._apply_css("common.css")

        if current_theme:
            ThemeManager._apply_dark_mode()
        else:
            ThemeManager._apply_light_mode()

    @staticmethod
    def _apply_dark_mode():
        ThemeManager._apply_css("dark_general.css")
        ThemeManager._apply_css("dark_selectbox.css")
        ThemeManager._apply_css("dark_file_uploader.css")

    @staticmethod
    def _apply_light_mode():
        ThemeManager._apply_css("light_general.css")
        ThemeManager._apply_css("light_selectbox.css")
        ThemeManager._apply_css("light_file_uploader.css")

    @staticmethod
    def _apply_css(filename):
        css_path = os.path.join(ThemeManager.BASE_DIR, "..", "assets", "theme", filename)
        if os.path.exists(css_path):
            with open(css_path, "r", encoding="utf-8") as f:
                st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)
        else:
            st.warning(f"⚠️ CSS file not found: {filename}")

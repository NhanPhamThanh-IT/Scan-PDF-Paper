import streamlit as st
from pathlib import Path

class ThemeManager:
    THEME_DIR = Path(__file__).resolve().parent.parent / "assets" / "themes"

    @staticmethod
    def apply():
        ThemeManager._apply_css_file("common.css")

    @staticmethod
    def _apply_css_file(file_name: str):
        ThemeManager._apply_css(ThemeManager.THEME_DIR / file_name)

    @staticmethod
    def _apply_css(file_path: Path):
        if file_path.exists():
            with open(file_path, "r", encoding="utf-8") as f:
                css = f.read()
            st.markdown(f"<style>{css}</style>", unsafe_allow_html=True)
        else:
            raise FileNotFoundError(f"CSS file {file_path} not found.")
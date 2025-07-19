import streamlit as st
from pathlib import Path

class ThemeManager:
    THEME_DIR = Path(__file__).resolve().parent.parent / "assets" / "theme"

    @staticmethod
    def apply():
        current_theme = st.session_state.get("dark_mode", False)
        if st.session_state.get("_theme_applied") == current_theme:
            return

        ThemeManager._apply_css_file("common.css")
        mode_dir = "dark_mode" if current_theme else "light_mode"
        ThemeManager._apply_css_folder(mode_dir)

        st.session_state["_theme_applied"] = current_theme

    @staticmethod
    def _apply_css_folder(folder_name: str):
        folder_path = ThemeManager.THEME_DIR / folder_name
        if not folder_path.exists():
            st.warning(f"⚠️ Theme folder not found: {folder_name}")
            return

        for css_file in sorted(folder_path.glob("*.css")):
            ThemeManager._apply_css(css_file)

    @staticmethod
    def _apply_css_file(file_name: str):
        ThemeManager._apply_css(ThemeManager.THEME_DIR / file_name)

    @staticmethod
    def _apply_css(path: Path):
        if not path.exists():
            st.warning(f"⚠️ CSS file not found: {path.name}")
            return

        with path.open("r", encoding="utf-8") as f:
            st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

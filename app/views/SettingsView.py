import streamlit as st
from settings import ThemeManager

class SettingsView:
    @staticmethod
    def render():
        ThemeManager.apply()
        
        if "dark_mode" not in st.session_state:
            st.session_state.dark_mode = False
        if "_theme_applied" not in st.session_state:
            st.session_state._theme_applied = None

        st.title("Settings")
        st.markdown("Customize the behavior and appearance of the PDF Topic Analyzer below.")
        st.subheader("Appearance Settings")

        dark_mode = st.toggle("🌙 Enable Dark Mode", value=st.session_state.dark_mode)

        if dark_mode != st.session_state.dark_mode:
            st.session_state.dark_mode = dark_mode
            st.rerun()

import streamlit as st

class SettingsView:
    @staticmethod
    def render():
        st.markdown("Customize the behavior and appearance of the PDF Topic Analyzer below.")
        st.subheader("Appearance Settings")

        SettingsView.handle_dark_mode_toggle()

    @staticmethod
    def handle_dark_mode_toggle():
        st.session_state.setdefault("dark_mode", False)
        st.session_state.setdefault("_theme_applied", None)

        dark_mode = st.toggle("🌙 Enable Dark Mode", value=st.session_state.dark_mode)
        if dark_mode != st.session_state.dark_mode:
            st.session_state.dark_mode = dark_mode
            st.rerun()

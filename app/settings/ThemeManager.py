import streamlit as st

class ThemeManager:
    @staticmethod
    def apply():
        """
        Apply dark/light theme once per change.
        """
        current_theme = st.session_state.get("dark_mode", False)
        last_applied = st.session_state.get("_theme_applied")

        if current_theme != last_applied:
            ThemeManager._apply_common_styles()
            if current_theme:
                ThemeManager._apply_dark_mode()
            else:
                ThemeManager._apply_light_mode()

            st.session_state["_theme_applied"] = current_theme

    @staticmethod
    def _apply_common_styles():
        """
        Apply shared styles regardless of theme.
        """
        st.markdown("""
            <style>
                header {visibility: hidden;}
                .streamlit-footer {display: none;}
                .st-emotion-cache-uf99v8 {display: none;}
                div .block-container {
                    padding: 0rem !important;
                    margin: 0rem !important;}
            </style>
        """, unsafe_allow_html=True)

    @staticmethod
    def _apply_dark_mode():
        st.markdown("""
            <style>
                .stApp {
                    background-color: #121212;
                    color: white;
                }
                .stMarkdown, .stTextInput, .stButton, .stSelectbox, .stDataFrame {
                    color: white !important;
                }
                .css-1v3fvcr {
                    background-color: #1e1e1e !important;
                }
                .css-1d391kg {
                    color: white !important;
                }
                .stHeader, h1, h2, h3, h4, h5, h6 {
                    color: white !important;
                }
            </style>
        """, unsafe_allow_html=True)

    @staticmethod
    def _apply_light_mode():
        st.markdown("""
            <style>
                .stApp {
                    background-color: white;
                    color: black;
                }
                .stMarkdown, .stTextInput, .stButton, .stSelectbox, .stDataFrame {
                    background-color: white !important;
                    color: black !important;
                }
                .css-1v3fvcr {
                    background-color: white !important;
                }
                .css-1d391kg {
                    color: black !important;
                }
                h1, h2, h3, h4, h5, h6 {
                    color: black !important;
                }
            </style>
        """, unsafe_allow_html=True)

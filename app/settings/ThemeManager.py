import streamlit as st

class ThemeManager:
    @staticmethod
    def apply():
        current_theme = st.session_state.get("dark_mode", False)
        ThemeManager._apply_common_styles()
        if current_theme:
            ThemeManager._apply_dark_mode()
        else:
            ThemeManager._apply_light_mode()

    @staticmethod
    def _apply_common_styles():
        st.markdown("""
            <style>
                header {visibility: hidden;}
                .streamlit-footer {display: none;}
                .st-emotion-cache-uf99v8 {display: none;}
                div .block-container {
                    padding: 0rem !important;
                    margin: 0rem !important;
                }
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
                .stMarkdown, .stTextInput, .stButton, .stDataFrame {
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
                div[data-baseweb="select"] > div {
                    background-color: #2c2c2c !important;
                    color: white !important;
                    border: 1px solid #555;
                    border-radius: 6px;
                }
                div[data-baseweb="select"] span {
                    color: white !important;
                }
                div[data-baseweb="popover"] {
                    background-color: #2c2c2c !important;
                    color: white !important;
                }
                div[data-baseweb="option"]:hover {
                    background-color: #3a3a3a !important;
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
                .stMarkdown, .stTextInput, .stButton, .stDataFrame {
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
                div[data-baseweb="select"] > div {
                    background-color: #f0f0f0 !important;
                    color: black !important;
                    border-radius: 6px;
                    border: 1px solid #ccc;
                }
                div[data-baseweb="select"] span {
                    color: black !important;
                }
                div[data-baseweb="popover"] {
                    background-color: #f9f9f9 !important;
                    color: black !important;
                }
                div[data-baseweb="option"]:hover {
                    background-color: #e0e0e0 !important;
                }
            </style>
        """, unsafe_allow_html=True)

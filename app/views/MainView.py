import streamlit as st
import os
from settings import ThemeManager
from core import FileHandling, TextHandling, DataHandling
from ui import ResultComponent

class MainView:
    BASE_DIR = os.path.dirname(os.path.dirname(__file__))
    DATA_PATH = os.path.join(BASE_DIR, "data", "topics_keywords")
    TOPICS = DataHandling.load_local_topics_data(DATA_PATH)

    @staticmethod
    def render():
        """
        Static method to render the main view.
        """
        ThemeManager.apply()

        topics = MainView._render_topic_selector()
        uploaded_file = MainView._render_file_uploader()

        if not uploaded_file or not topics:
            return

        with st.spinner("Extracting and analyzing text..."):
            result = MainView._analyze_pdf(uploaded_file, topics)

        ResultComponent(result).render()

    @staticmethod
    def _render_topic_selector():
        return st.selectbox("Select a topic", list(MainView.TOPICS.keys()))

    @staticmethod
    def _render_file_uploader():
        return st.file_uploader("Choose a PDF file", type="pdf")

    @staticmethod
    def _analyze_pdf(uploaded_file, topic):
        text = FileHandling.extract_text_from_pdf(uploaded_file)
        match_percent, keyword_count, total_words = TextHandling.calculate_topic_match(
            text, MainView.TOPICS[topic]
        )

        return {
            "total_words": total_words,
            "keyword_count": keyword_count,
            "match_percent": match_percent
        }

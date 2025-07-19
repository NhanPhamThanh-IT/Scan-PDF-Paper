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
        ThemeManager.apply()
        
        topic = MainView._render_topic_selector()
        file = MainView._render_file_uploader()

        if not file or not topic:
            return

        with st.spinner("Extracting and analyzing text..."):
            result = MainView._analyze_pdf(file, topic)

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
        result = TextHandling.calculate_topic_match(text, MainView.TOPICS[topic])
        return dict(zip(["match_percent", "keyword_count", "total_words"], result))


import streamlit as st
import os
from core import FileHandling, TextHandling, DataHandling
from ui import PageHeaderComponent, ResultComponent

class MainPage:
    BASE_DIR = os.path.dirname(os.path.dirname(__file__))
    DATA_PATH = os.path.join(BASE_DIR, "dataset", "topics_keywords")
    TOPICS = DataHandling.load_local_topics_data(DATA_PATH)

    @staticmethod
    def render():
        MainPage._render_page_header()

        topic = MainPage._render_topic_selector()
        file = MainPage._render_file_uploader()

        if not file or not topic:
            return

        with st.spinner("Extracting and analyzing text..."):
            result = MainPage._analyze_pdf(file, topic)

        ResultComponent(title=f"Analysis Results", analysis_result=result).render()

    @staticmethod
    def _render_page_header():
        PageHeaderComponent(
            title="Main Page",
        ).render()

    @staticmethod
    def _render_topic_selector():
        return st.selectbox("Select a topic", list(MainPage.TOPICS.keys()))

    @staticmethod
    def _render_file_uploader():
        return st.file_uploader("Choose a PDF file", type=["pdf", "docx", 'txt'])

    @staticmethod
    def _analyze_pdf(uploaded_file, topic):
        text = FileHandling.extract_text_from_file(uploaded_file)
        result = TextHandling.calculate_topic_match(text, MainPage.TOPICS[topic])
        return result
    
if __name__ == "__main__":
    st.set_page_config(page_title="Main Page")
    MainPage.render()
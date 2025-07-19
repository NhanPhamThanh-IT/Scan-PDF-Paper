import streamlit as st
import os
from settings import ThemeManager
from core import FileHandling, TextHandling, DataHandling
from ui import ResultComponent

# Load topic data
BASE_DIR = os.path.dirname(os.path.dirname(__file__))
DATA_PATH = os.path.join(BASE_DIR, "data", "topics_keywords")
TOPICS = DataHandling.load_local_topics_data(DATA_PATH)

def render_main_view():
    ThemeManager.apply()

    topic = st.selectbox("Select a topic", list(TOPICS.keys()))
    uploaded_file = st.file_uploader("Choose a PDF file", type="pdf")

    if not uploaded_file or not topic:
        return

    with st.spinner("Extracting and analyzing text..."):
        text = FileHandling.extract_text_from_pdf(uploaded_file)
        match_percent, keyword_count, total_words = TextHandling.calculate_topic_match(
            text, TOPICS[topic]
        )

    ResultComponent({
        "total_words": total_words,
        "keyword_count": keyword_count,
        "match_percent": match_percent
    }).render()
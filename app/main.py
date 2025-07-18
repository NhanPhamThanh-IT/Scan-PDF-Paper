import os
import sys
import streamlit as st

# Add current directory to sys.path for module resolution
BASE_DIR = os.path.dirname(__file__)
sys.path.append(BASE_DIR)

# Local imports
from core import DataHandling, FileHandling, TextHandling
from ui import ResultView

# Load topic data
DATA_PATH = os.path.join(BASE_DIR, "data", "topics_keywords")
TOPICS = DataHandling.load_local_topics_data(DATA_PATH)


def run_app():
    st.markdown(
        "<h1 style='text-align: center;'>PDF Topic Analyzer</h1>",
        unsafe_allow_html=True
    )

    topic = st.selectbox("Select a topic", list(TOPICS.keys()))
    uploaded_file = st.file_uploader("Choose a PDF file", type="pdf")

    if not uploaded_file or not topic:
        return

    with st.spinner("Extracting and analyzing text..."):
        text = FileHandling.extract_text_from_pdf(uploaded_file)
        match_percent, keyword_count, total_words = TextHandling.calculate_topic_match(
            text, TOPICS[topic]
        )

    analysis_result = {
        "total_words": total_words,
        "keyword_count": keyword_count,
        "match_percent": match_percent
    }

    ResultView(analysis_result).render()


if __name__ == "__main__":
    run_app()

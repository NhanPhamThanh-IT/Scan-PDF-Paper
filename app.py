import streamlit as st
from utils import FileHandling, TextHandling

TOPICS = FileHandling.load_data_from_json("data/topics_keywords.json")

def draw_analysis_result(analysis_result: dict):
    st.markdown("<h3 style='text-align: center;'>Analysis Result</h3>", unsafe_allow_html=True)
    cols = st.columns(len(analysis_result))

    for col, (key, value) in zip(cols, analysis_result.items()):
        label = key.replace("_", " ").title()
        if any(kw in key.lower() for kw in ["percent", "match"]):
            display_value = f"{value}%" if isinstance(value, (int, float)) else str(value)
        else:
            display_value = value

        col.markdown(f"""
            <div style='text-align: center; padding: 10px; border: 1px solid #ddd; border-radius: 10px; background-color: #f9f9f9;'>
                <div style='font-size: 16px; color: #555;'>{label}</div>
                <div style='font-size: 22px; font-weight: bold; color: #222;'>{display_value}</div>
            </div>
        """, unsafe_allow_html=True)

def run_app():
    st.markdown("<h1 style='text-align: center;'>PDF Topic Analyzer</h1>", unsafe_allow_html=True)

    topic = st.selectbox("Select a topic", list(TOPICS.keys()))
    uploaded_file = st.file_uploader("Choose a PDF file", type="pdf")

    if uploaded_file is not None and topic:
        with st.spinner("Extracting and analyzing text..."):
            text = FileHandling.extract_text_from_pdf(uploaded_file)
            match_percent, keyword_count, total_words = TextHandling.calculate_topic_match(text, TOPICS[topic])

        analysis_result = {
            "total_words": total_words,
            "keyword_count": keyword_count,
            "match_percent": match_percent
        }
        draw_analysis_result(analysis_result)

if __name__ == "__main__":
    run_app()

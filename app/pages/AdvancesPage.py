import streamlit as st
from ui import PageHeaderComponent, ResultComponent
from core import FileHandling, TopicClassifier

class AdvancesPage:

    @staticmethod
    def render():
        AdvancesPage._render_page_header()
                
        file = AdvancesPage._render_file_uploader()
        if not file:
            return
        with st.spinner("Processing..."):
            try:
                content = FileHandling.extract_text_from_file(file)
                if not content:
                    st.error("No text found in the uploaded file.")
                    return

                top_topics = TopicClassifier.get_top_topics(content)
                ResultComponent(title="Top Topics", analysis_result=top_topics).render()

            except ValueError as e:
                st.error(f"Error processing file: {e}")
            except Exception as e:
                st.error(f"An unexpected error occurred: {e}")

    @staticmethod
    def _render_page_header():
        PageHeaderComponent(
            title="Advanced Options",
        ).render()

    @staticmethod
    def _render_file_uploader():
        return st.file_uploader("Choose a PDF file", type=["pdf", "docx", 'txt'])

if __name__ == "__main__":
    st.set_page_config(page_title="Advanced Options")
    AdvancesPage.render()
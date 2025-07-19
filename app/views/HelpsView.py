import streamlit as st

class HelpsView:
    """
    A class to render the Helps view in a Streamlit application.
    This view provides instructions and information about how to use the app.
    """

    @staticmethod
    def render():
        """
        Displays the Helps page with usage instructions and notes.
        """
        st.markdown("""
            This application allows you to analyze PDF documents for specific topics.
            You can upload a PDF file and select a topic to see how well the document matches the topic based on keyword analysis.
            
            **Instructions:**

            &emsp;&emsp;1. Select a topic from the dropdown menu.

            &emsp;&emsp;2. Upload a PDF file using the file uploader.

            &emsp;&emsp;3. The application will extract text from the PDF and analyze it against the selected topic.

            &emsp;&emsp;4. Results will be displayed, including total words, keyword count, and match percentage.

            **Note:** Ensure that the PDF file is clear and contains relevant text for accurate analysis.
        """)

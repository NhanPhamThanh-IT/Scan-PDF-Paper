import fitz
import json

class FileHandling:
    @staticmethod
    def extract_text_from_pdf(file):
        pdf_document = fitz.open(stream=file.read(), filetype="pdf")
        text = ""
        for page in pdf_document:
            text += page.get_text()
        return text

    @staticmethod
    def load_data_from_json(file):
        with open(file, 'r', encoding='utf-8') as f:
            data = json.load(f)
        return data
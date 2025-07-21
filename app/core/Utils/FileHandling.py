import json
from typing import BinaryIO, Dict, List, Any, Callable
import fitz
from docx import Document

class FileHandling:
    @staticmethod
    def _open_pdf(file: BinaryIO) -> fitz.Document:
        return fitz.open(stream=file.read(), filetype="pdf")

    @staticmethod
    def _extract_images_from_page(page: fitz.Page) -> List[bytes]:
        return [
            page.parent.extract_image(img[0])["image"]
            for img in page.get_images(full=True)
        ]

    @staticmethod
    def extract_content_from_pdf(file: BinaryIO, text: bool = True, images: bool = True) -> Dict[str, Any]:
        pdf = FileHandling._open_pdf(file)
        result = {}

        if text:
            result["text"] = "".join(page.get_text() for page in pdf)

        if images:
            result["images"] = [
                img for page in pdf for img in FileHandling._extract_images_from_page(page)
            ]

        return result

    @staticmethod
    def extract_text_from_pdf(file: BinaryIO) -> str:
        return FileHandling.extract_content_from_pdf(file, text=True, images=False)["text"]

    @staticmethod
    def extract_images_from_pdf(file: BinaryIO) -> List[bytes]:
        return FileHandling.extract_content_from_pdf(file, text=False, images=True)["images"]

    @staticmethod
    def extract_text_from_docx(file: BinaryIO) -> str:
        try:
            doc = Document(file)
            paragraphs = [p.text.strip() for p in doc.paragraphs if p.text.strip()]
            return "\n".join(paragraphs)
        except Exception as e:
            raise ValueError(f"Failed to extract text from DOCX: {e}")

    @staticmethod
    def extract_text_from_txt(file: BinaryIO) -> str:
        try:
            return file.read().decode("utf-8").strip()
        except Exception as e:
            raise ValueError(f"Failed to extract text from TXT file: {e}")

    @staticmethod
    def extract_text_from_file(file: BinaryIO) -> str:
        extractors: Dict[str, Callable[[BinaryIO], str]] = {
            ".pdf": FileHandling.extract_text_from_pdf,
            ".docx": FileHandling.extract_text_from_docx,
            ".txt": FileHandling.extract_text_from_txt,
        }

        for ext, extractor in extractors.items():
            if file.name.endswith(ext):
                return extractor(file)

        raise ValueError("Unsupported file type. Supported: PDF, DOCX, TXT")

    @staticmethod
    def load_data_from_json(path: str) -> Any:
        with open(path, encoding="utf-8") as f:
            return json.load(f)

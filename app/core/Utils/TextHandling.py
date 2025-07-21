import re
from spacy.lang.en.stop_words import STOP_WORDS

class TextHandling:
    @staticmethod
    def preprocess(text: str) -> str:
        if not text or not isinstance(text, str):
            return ""

        words = re.findall(r"\b\w+\b", text.lower())
        filtered_words = [w for w in words if w not in STOP_WORDS]
        return " ".join(filtered_words)

    @staticmethod
    def calculate_topic_match(text, keywords):
        cleaned_text = TextHandling.preprocess(text)
        words = cleaned_text.split()
        total_words = len(words)

        word_freq = {}
        for w in words:
            word_freq[w] = word_freq.get(w, 0) + 1

        keyword_count = sum(word_freq.get(kw.lower(), 0) for kw in keywords)
        match_percent = (keyword_count / total_words) * 100 if total_words > 0 else 0

        return {
            "total_words": total_words,
            "keyword_count": keyword_count,
            "match_percent": round(match_percent, 3)
        }

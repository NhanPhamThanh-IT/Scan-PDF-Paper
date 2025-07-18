import re

class TextHandling:
    @staticmethod
    def calculate_topic_match(text, keywords):
        text = text.lower()
        words = re.findall(r"\b\w+\b", text)
        total_words = len(words)

        keyword_count = sum(text.count(kw.lower()) for kw in keywords)
        match_percent = (keyword_count / total_words) * 100 if total_words > 0 else 0

        return round(match_percent, 3), keyword_count, total_words
from sentence_transformers import SentenceTransformer, util
import torch
from typing import List, Tuple
from core.Utils import FileHandling


class TopicClassifier:
    _model = SentenceTransformer('all-MiniLM-L6-v2')

    try:
        TOPICS: List[str] = FileHandling.load_data_from_json("app/dataset/metadata/topics.json")
        _TOPIC_EMBEDDINGS = _model.encode(TOPICS, convert_to_tensor=True)
    except Exception as e:
        raise RuntimeError(f"⚠️ Failed to load topics or compute embeddings: {e}")

    @staticmethod
    def classify(text: str) -> str:
        if not text.strip():
            return "Unknown"

        text_embedding = TopicClassifier._model.encode(text, convert_to_tensor=True)
        cosine_scores = util.cos_sim(text_embedding, TopicClassifier._TOPIC_EMBEDDINGS)
        best_index = torch.argmax(cosine_scores).item()
        return TopicClassifier.TOPICS[best_index]

    @staticmethod
    def get_top_topics(text: str, top_k: int = 3) -> List[Tuple[str, float]]:
        if not text.strip():
            return [("Unknown", 0.0)]

        text_embedding = TopicClassifier._model.encode(text, convert_to_tensor=True)
        cosine_scores = util.cos_sim(text_embedding, TopicClassifier._TOPIC_EMBEDDINGS).squeeze()

        normalized = (cosine_scores / cosine_scores.sum()) * 100
        top_indices = torch.topk(normalized, k=top_k).indices.tolist()
        return {TopicClassifier.TOPICS[i]: f'{round(normalized[i].item(), 2)}%' for i in top_indices}

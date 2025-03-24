
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import numpy as np

class Text_Similarity:
    def __init__(self):
        self.vectorizer = TfidfVectorizer()

    def tfid_calc(self, texts, user_text):
        corpus = list(texts.values())
        corpus.append(user_text)

        tfid_matrix = self.vectorizer.fit_transform(corpus)
        cos_sim_matrix = cosine_similarity(tfid_matrix[-1], tfid_matrix[:-1])

        threshold  = np.percentile(cos_sim_matrix, 90)
        fallback_threshold = 0.3
        print(f"Threshold: {threshold:.4f}")

        for num, similarity in enumerate(cos_sim_matrix[0]):
            print(f"Similarity with {list(texts.keys())[num]}: {similarity:.4f}")
            if similarity > threshold and similarity > fallback_threshold:
                print(f"Similarity detected between provided text and {list(texts.keys())[num]} with similarity of {similarity:.4f}\n\n")

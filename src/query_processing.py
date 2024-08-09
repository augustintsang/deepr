# src/query_processing.py
from sentence_transformers import SentenceTransformer
from sklearn.metrics.pairwise import cosine_similarity
import pandas as pd
import numpy as np
from config import config

model = SentenceTransformer(config.MODEL_PATH)
embeddings = pd.read_csv(config.EMBEDDINGS_PATH).values

def encode_query(query):
    return model.encode([query])

def search_similar(query_embedding, top_k=10):
    similarities = cosine_similarity(query_embedding, embeddings)
    top_k_indices = np.argsort(similarities[0])[-top_k:][::-1]
    return top_k_indices
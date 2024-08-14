# src/model_training.py
import json
import pandas as pd
from sentence_transformers import SentenceTransformer
from config import config

def load_mock_db():
    with open('data/mock_db.json', 'r') as f:
        return json.load(f)

def load_data_from_mock_db():
    db = load_mock_db()
    data = pd.DataFrame(db['songs'])
    return data

def train_and_encode(data):
    model = SentenceTransformer('distilbert-base-nli-stsb-mean-tokens')
    titles_and_artists = data['title'].tolist() + data['primary_artist'].tolist()
    embeddings = model.encode(titles_and_artists)
    pd.DataFrame(embeddings).to_csv(config.EMBEDDINGS_PATH)
    model.save(config.MODEL_PATH)

if __name__ == "__main__":
    data = load_data_from_mock_db()
    train_and_encode(data)

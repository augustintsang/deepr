# config.py
import os

class Config:
    DATABASE_URI = os.getenv('DATABASE_URI', 'mysql://user:password@host/database')
    EMBEDDINGS_PATH = os.getenv('EMBEDDINGS_PATH', 'data/embeddings/embeddings.csv')
    MODEL_PATH = os.getenv('MODEL_PATH', 'models/sentence_transformer/')
    FLASK_ENV = os.getenv('FLASK_ENV', 'development')
    FLASK_DEBUG = os.getenv('FLASK_DEBUG', True)

config = Config()
# tests/test_model_training.py
import unittest
import pandas as pd
from src.model_training import train_and_encode
from config import config

class TestModelTraining(unittest.TestCase):

    def test_train_and_encode(self):
        # Create a small dataset for testing
        data = pd.DataFrame({
            'title': ["Shape of You", "Smooth"],
            'primary_artist': ["Ed Sheeran", "Santana"]
        })
        
        # Run the training and encoding
        train_and_encode(data)
        
        # Check that embeddings are saved
        embeddings = pd.read_csv(config.EMBEDDINGS_PATH)
        self.assertEqual(embeddings.shape[0], 2)

if __name__ == '__main__':
    unittest.main()

# tests/test_data_ingestion.py
import unittest
import json
from src.data_ingestion import store_raw_data_in_mock_db, clean_and_transform_mock_data

class TestDataIngestion(unittest.TestCase):

    def setUp(self):
        # Load the mock database
        with open('data/mock_db.json', 'r') as f:
            self.db = json.load(f)

    def tearDown(self):
        # Restore the original mock database state
        with open('data/mock_db.json', 'w') as f:
            json.dump(self.db, f, indent=4)

    def test_store_raw_data_in_mock_db(self):
        new_data = [
            {
                "id": "5",
                "title": "New Song Title",
                "primary_artist": "New Artist",
                "album": "New Album",
                "processed": False
            }
        ]
        store_raw_data_in_mock_db(new_data)
        db = load_mock_db()
        self.assertEqual(len(db['songs']), 5)

    def test_clean_and_transform_mock_data(self):
        clean_and_transform_mock_data()
        db = load_mock_db()
        processed_songs = [song for song in db['songs'] if song['processed']]
        self.assertEqual(len(processed_songs), 4)

if __name__ == '__main__':
    unittest.main()

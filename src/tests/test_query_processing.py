# tests/test_query_processing.py
import unittest
from src.query_processing import encode_query, search_similar
from flask import Flask
from src.api import app

class TestQueryProcessing(unittest.TestCase):

    def test_encode_query(self):
        query = "Shape of You"
        query_embedding = encode_query(query)
        self.assertEqual(len(query_embedding), 1)

    def test_search_similar(self):
        query = "Shape of You"
        query_embedding = encode_query(query)
        results = search_similar(query_embedding)
        self.assertTrue(len(results) > 0)

class TestAPI(unittest.TestCase):

    def setUp(self):
        self.app = app.test_client()
        self.app.testing = True

    def test_search_endpoint(self):
        response = self.app.get('/search?query=Shape of You')
        self.assertEqual(response.status_code, 200)
        self.assertIn('Shape of You', str(response.data))

if __name__ == '__main__':
    unittest.main()
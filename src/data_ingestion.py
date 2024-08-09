# src/data_ingestion.py
import json

def load_mock_db():
    with open('data/mock_db.json', 'r') as f:
        return json.load(f)

def save_mock_db(db):
    with open('data/.json', 'w') as f:
        json.dump(db, f, indent=4)

def store_raw_data_in_mock_db(data):
    db = load_mock_db()
    db['songs'].extend(data)
    save_mock_db(db)

def clean_and_transform_mock_data():
    db = load_mock_db()
    for song in db['songs']:
        song['title'] = song['title'].strip()
        song['primary_artist'] = song['primary_artist'].strip()
        song['processed'] = True
    save_mock_db(db)

if __name__ == "__main__":
    # Simulating data ingestion using the mock database
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
    clean_and_transform_mock_data()

from sentence_transformers import SentenceTransformer, util
import numpy as np

# Initialize the Sentence Transformer model
model = SentenceTransformer('all-MiniLM-L6-v2')

def standardize_artist_names(artist_names):
    embeddings = model.encode(artist_names, convert_to_tensor=True)
    reference_embedding = embeddings[0]
    similarities = util.pytorch_cos_sim(reference_embedding, embeddings)
    
    # Move the similarities tensor to CPU and convert it to a NumPy array
    similarities_cpu = similarities.cpu().numpy()
    
    # Find the index of the most similar name
    standard_name = artist_names[np.argmax(similarities_cpu)]
    return standard_name

def fill_in_missing_artist(incomplete_data, possible_artists):
    artist_embeddings = model.encode(possible_artists, convert_to_tensor=True)
    incomplete_embedding = model.encode(incomplete_data, convert_to_tensor=True)
    
    # Calculate similarities and move to CPU
    similarities = util.pytorch_cos_sim(incomplete_embedding, artist_embeddings)
    similarities_cpu = similarities.cpu().numpy()
    
    # Find the best match
    best_artist = possible_artists[np.argmax(similarities_cpu)]
    return f"{incomplete_data} {best_artist}"

def find_best_match(search_query, song_options):
    song_embeddings = model.encode(song_options, convert_to_tensor=True)
    query_embedding = model.encode(search_query, convert_to_tensor=True)

    # Calculate similarities and move to CPU
    similarities = util.pytorch_cos_sim(query_embedding, song_embeddings)
    similarities_cpu = similarities.cpu().numpy()

    # Find the best match
    best_match = song_options[np.argmax(similarities_cpu)]
    return best_match

def rank_songs_by_metadata(song_options, metadata):
    ranked_options = sorted(song_options, key=lambda x: (metadata[x]["popularity"], metadata[x]["release_year"]), reverse=True)
    return ranked_options

def standardize_data(data_sources, standard_entry):
    standardized_data = []
    standard_embedding = model.encode(standard_entry, convert_to_tensor=True)
    
    for entry in data_sources:
        input_text = f"{entry['artist']} - {entry['title']}"
        embedding = model.encode(input_text, convert_to_tensor=True)
        standardized_data.append((input_text, embedding))
    
    corrected_data = []
    for i, (text, embedding) in enumerate(standardized_data):
        similarity = util.pytorch_cos_sim(standard_embedding, embedding)
        if similarity < 0.95:
            print(f"Inconsistency detected: {text}")
            corrected_data.append(standard_entry)
        else:
            corrected_data.append(text)
    
    return corrected_data

def main():
    # Problem 0: Standardize Artist Names 
    artist_names = ["Ed Sheeran", "E. Sheeran", "Edward Sheeran"]
    standardized_name = standardize_artist_names(artist_names)
    print("Standardized Artist Name:", standardized_name)

    # Problem 1: Fill in Missing Artist
    incomplete_data = "Shape of You by"
    possible_artists = ["Ed Sheeran", "Adele", "Beyoncé"]
    completed_data = fill_in_missing_artist(incomplete_data, possible_artists)
    print("Completed Data:", completed_data)

    # Problem 2: Find Best Match for Ambiguous Title
    search_query = "Alone"
    song_options = [
        "Alone by Alan Walker",
        "Alone by Marshmello",
        "Alone by Halsey"
    ]
    best_match = find_best_match(search_query, song_options)
    print("Best Match for Search Query:", best_match)

    # Problem 2: Rank Songs by Metadata
    metadata = {
        "Alone by Alan Walker": {"popularity": 95, "release_year": 2016},
        "Alone by Marshmello": {"popularity": 85, "release_year": 2018},
        "Alone by Halsey": {"popularity": 90, "release_year": 2020},
    }
    ranked_results = rank_songs_by_metadata(song_options, metadata)
    print("Ranked Search Results:", ranked_results)

    # Problem 3: Standardize and Clean Data from Different Sources
    data_sources = [
        {"source": "Spotify", "artist": "E. Sheeran", "title": "Shape of You"},
        {"source": "Apple Music", "artist": "Edward Sheeran", "title": "Shape Of You"},
        {"source": "YouTube", "artist": "Ed Sheeran", "title": "Shape of You"}
    ]
    standard_entry = "Ed Sheeran - Shape of You"
    standardized_data = standardize_data(data_sources, standard_entry)
    print("Standardized Data Entries:", standardized_data)

if __name__ == "__main__":
    main()

# src/api.py
from api import Flask, request, jsonify
from query_processing import encode_query, search_similar
import pandas as pd

app = Flask(__name__)

@app.route('/search', methods=['GET'])
def search():
    query = request.args.get('query')
    query_embedding = encode_query(query)
    results_indices = search_similar(query_embedding)
    results = data.iloc[results_indices]
    return jsonify(results.to_dict(orient='records'))

if __name__ == '__main__':
    data = pd.read_sql("SELECT title, primary_artist FROM songs", con=db_connection)
    app.run(debug=config.FLASK_DEBUG)

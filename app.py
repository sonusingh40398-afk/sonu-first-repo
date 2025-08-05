from flask import Flask, request, jsonify
import requests

app = Flask(__name__)

OPEN_SOURCE_URL = "https://jsonplaceholder.typicode.com/users"

@app.route('/sorted-data', methods=['GET'])
def get_sorted_data():
    sort_key = request.args.get('sort_by', default='id')

    try:
        response = requests.get(OPEN_SOURCE_URL)
        response.raise_for_status()
        data = response.json()

        if not data or sort_key not in data[0]:
            return jsonify({"error": f"Invalid sort key: '{sort_key}'"}), 400

        sorted_data = sorted(data, key=lambda item: item.get(sort_key))
        return jsonify(sorted_data)

    except requests.exceptions.RequestException as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)

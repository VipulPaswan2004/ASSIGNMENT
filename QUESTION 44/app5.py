from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/api/data', methods=['GET'])
def get_data():
    # Define the data to be returned as JSON
    data = {
        'name': 'Vipul',
        'age': 22,
        'city': 'New Delhi'
    }
    # Return the data as a JSON response
    return jsonify(data)

if __name__ == '__main__':
    app.run(debug=True)

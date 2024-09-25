from flask import Flask, request

app = Flask(__name__)

# Define a route that accepts a string parameter from the URL
@app.route('/greet/<name>')
def greet(name):
    # Input validation: Check if name is a string
    if not isinstance(name, str):
        return "Error: Name must be a string", 400
    
    # Return a greeting message
    return f"Hello, {name}!"

if __name__ == '__main__':
    app.run(debug=True)
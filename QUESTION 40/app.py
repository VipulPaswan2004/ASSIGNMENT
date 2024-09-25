from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/submit', methods=['POST'])
def submit():
    # Retrieve form data
    name = request.form['name']
    email = request.form['email']
    
    # Process the data (e.g., print it)
    return f"Name: {name}, Email: {email}"

if __name__ == '__main__':
    app.run(debug=True)

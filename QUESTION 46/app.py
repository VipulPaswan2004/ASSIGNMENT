from flask import Flask, request, render_template, redirect, url_for
import os

app = Flask(__name__)

# Set the directory where uploaded files will be saved
UPLOAD_FOLDER = 'uploads'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

# Ensure the upload folder exists
if not os.path.exists(UPLOAD_FOLDER):
    os.makedirs(UPLOAD_FOLDER)

@app.route('/')
def index():
    return render_template('index.html')

# Handle file uploads
@app.route('/upload', methods=['POST'])
def upload_file():
    if 'file' not in request.files:
        return "No file part in the request."
    
    file = request.files['file']
    
    if file.filename == '':
        return "No selected file."
    
    if file:
        # Save the file to the upload directory
        filepath = os.path.join(app.config['UPLOAD_FOLDER'], file.filename)
        file.save(filepath)
        return f"File uploaded successfully: {file.filename}"

if __name__ == '__main__':
    app.run(debug=True)

from flask import Flask, render_template, request, redirect, url_for, session, flash
from flask_bcrypt import Bcrypt
from pymongo import MongoClient

app = Flask(__name__)
app.secret_key = 'supersecretkey'
bcrypt = Bcrypt(app)

# MongoDB connection
client = MongoClient('mongodb://localhost:27017/')
db = client['flask_login']
users = db['users']

@app.route('/')
def home():
    if 'username' in session:
        return render_template('home.html', username=session['username'])
    return redirect(url_for('login'))

@app.route('/signup', methods=['GET', 'POST'])
def signup():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        existing_user = users.find_one({'username': username})

        if existing_user is None:
            hashpass = bcrypt.generate_password_hash(password).decode('utf-8')
            users.insert_one({'username': username, 'password': hashpass})
            session['username'] = username
            return redirect(url_for('home'))
        flash('Username already exists!')

    return render_template('signup.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        user = users.find_one({'username': username})

        if user and bcrypt.check_password_hash(user['password'], password):
            session['username'] = username
            return redirect(url_for('home'))
        flash('Invalid username/password combination.')

    return render_template('login.html')

@app.route('/logout')
def logout():
    session.pop('username', None)
    return redirect(url_for('login'))

if __name__ == '__main__':
    app.run(debug=True)

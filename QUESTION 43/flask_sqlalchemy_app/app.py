from flask import Flask
from models import db, User  # Import the SQLAlchemy instance and the User model

# Initialize Flask app
app = Flask(__name__)

# Configure the SQLite database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///users.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Link SQLAlchemy instance to the Flask app
db.init_app(app)

# Create the database tables when the app context is started
with app.app_context():
    db.create_all()

# Route for adding a new user (for testing purposes)
@app.route('/add_user/<username>/<email>')
def add_user(username, email):
    new_user = User(username=username, email=email)
    db.session.add(new_user)
    db.session.commit()
    return f'Added user {username} with email {email}'

# Route to get all users
@app.route('/users')
def get_users():
    users = User.query.all()
    return f'All users: {[user.username for user in users]}'

# Start the Flask app
if __name__ == '__main__':
    app.run(debug=True)

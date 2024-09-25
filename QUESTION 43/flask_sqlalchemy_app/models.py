from flask_sqlalchemy import SQLAlchemy

# Initialize the SQLAlchemy instance (only once)
db = SQLAlchemy()

# Define the User model
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)  # Unique ID for each user
    username = db.Column(db.String(80), unique=True, nullable=False)  # Username field
    email = db.Column(db.String(120), unique=True, nullable=False)  # Email field

    def __repr__(self):
        return f'<User {self.username}>'

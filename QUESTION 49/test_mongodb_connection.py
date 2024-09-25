from pymongo import MongoClient, errors

try:
    client = MongoClient('mongodb://localhost:27017/', serverSelectionTimeoutMS=5000)
    db = client['flask_login']
    # Attempt to fetch server info to trigger an immediate connection attempt
    client.server_info()
    print("Connected to MongoDB successfully!")
except errors.ServerSelectionTimeoutError as err:
    print("Failed to connect to MongoDB:", err)

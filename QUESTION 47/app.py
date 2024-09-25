from flask import Flask
from auth_bp import auth  # Import the 'auth' blueprint from the renamed folder

app = Flask(__name__)

# Register the blueprint
app.register_blueprint(auth, url_prefix='/auth')

@app.route('/')
def home():
    return "Home Page"

if __name__ == '__main__':
    app.run(debug=True)
    
"""Why Use Flask Blueprints?

Modularity: Blueprints allow you to break down your application into smaller, manageable components, like separate modules for authentication, admin, or user functionality. This makes it easier to maintain and understand the code.

Reusability: If you're working on multiple projects or a large codebase, blueprints can be reused across different projects or applications.

Team Collaboration: Blueprints help teams collaborate by allowing developers to work on different parts of the application independently, without interfering with each other's code.

Organization: By organizing routes and logic into separate blueprints, your project structure becomes more organized, making it easier to scale the application as it grows.

Namespace separation: Blueprints provide an easy way to group related routes, keeping different sections of the application logically separate, but still allowing them to work together as part of the main app."""
from flask import Flask, request

app = Flask(__name__)

# Home route
@app.route('/home')
def home():
    return "Welcome to the Home Page", 200

# About route
@app.route('/about')
def about():
    return "About Us: This is the about page.", 200

# User route with dynamic username
@app.route('/users/<username>')
def user(username):
    return f"Profile of {username}", 200

# Posts route (GET and POST)
@app.route('/posts', methods=['GET', 'POST'])
def posts():
    if request.method == 'GET':
        # Simulate getting posts
        return "List of posts", 200
    elif request.method == 'POST':
        # Simulate creating a new post
        post_data = request.json
        return f"Post created: {post_data}", 201

# Post detail route with an integer post_id
@app.route('/posts/<int:post_id>')
def post(post_id):
    return f"Post {post_id}", 200

# Search route with a query parameter
@app.route('/search')
def search():
    query = request.args.get('query', '')
    return f"Search Results for '{query}'", 200

# 404 Error Handler for all other undefined routes
@app.errorhandler(404)
def page_not_found(error):
    return "Page not found", 404

if __name__ == '__main__':
    app.run(debug=True)

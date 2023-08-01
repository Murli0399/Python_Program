from flask import Flask, jsonify, request

app = Flask(__name__)

# Initialize a list to store posts. It currently contains one sample post.
list = [
    {'id':1,'username':'murli','caption':'any'}
]

# Endpoint to create a new post by sending a POST request with JSON data.
@app.route('/post', methods=['POST'])
def create():
    data = request.get_json()
    username = data.get('username')
    caption = data.get('caption')

    # Generate a new post dictionary with a unique ID.
    post = {
        'id': len(list) + 1,
        'username': username,
        'caption': caption 
    }

    # Append the new post to the list of posts.
    list.append(post)
    return jsonify(post)

# Endpoint to view all existing posts by sending a GET request.
@app.route('/allpost', methods=['GET'])
def view():
    return jsonify(list)

# Endpoint to delete a specific post by sending a DELETE request with the post ID.
@app.route('/delete/<int:pid>', methods=['DELETE'])
def deletePost(pid):
    data = {}
    for i in list:
        if i['id'] == pid:
            data = i
        else:
            data = None

    # If the post is found, remove it from the list and return the deleted post.
    if data:
        list.remove(data)
        return jsonify(data)
    else:
        return jsonify({'error': 'Post not found'})

if __name__ == '__main__':
    app.run()

# This is the main entry point of the application when running as a script.
# The Flask app is started and listens for incoming requests on localhost by default.

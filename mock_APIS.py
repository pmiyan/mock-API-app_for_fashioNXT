from flask import Flask, jsonify

app = Flask(__name__)

# Define a mock list of users
users = [
    {
        "name": "John Doe",
        "email": "johndoe@example.com",
        "location": "New York"
    },
    {
        "name": "Jane Smith",
        "email": "janesmith@example.com",
        "location": "Los Angeles"
    },
    {
        "name": "Bob Johnson",
        "email": "bobjohnson@example.com",
        "location": "Chicago"
    }
]

# Define a route to return the list of users
@app.route('/api/users')
def get_users():
    # Return the list of users as a JSON response
    return jsonify(users)

if __name__ == '__main__':
    app.run()

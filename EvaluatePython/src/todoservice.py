#
# Program: Task REST Service using Flask
#
# Start this web application running then type in relevent URL in browser to test each method
#

# Standard Python Library
import base64
import datetime
import os
from functools import wraps

# 3rd Party Libraries
import jwt
from flask import Flask, jsonify, abort, make_response, request
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Valid users for login
users = {
    os.environ.get('USERNAME'): os.environ.get('PASSWORD')
}

# Create a new Flask web application instance
app = Flask(__name__)

# Add configuration for the Flask app
app.config['SECRET_KEY'] = os.environ.get('SECRET_KEY')

# In-memory database
tasks = [
    {
        'id': 1,
        'title': 'Buy groceries',
        'description': 'Milk, Cheese, Pizza, Fruit, Tylenol',
        'done': False
    },
    {
        'id': 2,
        'title': 'Learn Python',
        'description': 'Need to find a good Python tutorial on the web',
        'done': False
    }
]

#
# Decorator to check for valid token in request header
#
def token_required(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        token = None
        if 'Authorization' in request.headers:
            token = request.headers['Authorization'].split(" ")[1]

        if not token:
            return jsonify({'message': 'Token is missing'}), 401

        try:
            data = jwt.decode(token, app.config['SECRET_KEY'], algorithms=['HS256'])
            current_user = data['user_id']
        except jwt.ExpiredSignatureError:
            return jsonify({'message': 'Token has expired'}), 401
        except jwt.InvalidTokenError:
            return jsonify({'message': 'Token is invalid'}), 401

        return f(current_user, *args, **kwargs)

    return decorated


#
# Error Handler for 404
#
@app.errorhandler(404)
def not_found(error):
    return make_response(jsonify({'error': 'Not found', 'detail': str(error)}), 404)

#
# GET ALL Method
#
# URL: http://localhost:5000/todo/api/v1.0/tasks
#
@app.route('/todo/api/v1.0/tasks', methods=['GET'])
@token_required
def get_tasks(current_user):
    print(f"get_tasks: Valid bearer token for user = {current_user}")
    return jsonify({'tasks': tasks})

#
# GET ID Method
#
# URL: http://localhost:5000/todo/api/v1.0/tasks/2
#
@app.route('/todo/api/v1.0/tasks/<int:task_id>', methods=['GET'])
@token_required
def get_task(current_user, task_id):
    print(f"get_task: Valid bearer token for user = {current_user}")
    task = [task for task in tasks if task['id'] == task_id]
    if len(task) == 0:
        abort(404)
    return jsonify({'task': task[0]})

#
# POST Method
#
# URL: http://localhost:5000/todo/api/v1.0/tasks
#
# HTTP Header:
# Content-Type = application/json
# HTTP Request:
# Body = {"title":"Remove ivy from garage wall"}
#
@app.route('/todo/api/v1.0/tasks', methods=['POST'])
@token_required
def create_task(current_user):
    print(f"create_task: Valid bearer token for user = {current_user}")
    if not request.json or not 'title' in request.json:
        abort(400)
    task = {
        'id': tasks[-1]['id'] + 1,
        'title': request.json['title'],
        'description': request.json.get('description', ""),
        'done': False
    }
    tasks.append(task)
    return jsonify({'task': task}), 201

#
# PUT ID Method
#
# URL: http://localhost:5000/todo/api/v1.0/tasks/1
#
# HTTP Header:
# Content-Type = application/json
# HTTP Request:
# Body = {"id":"1","title":"Buy groceries and beer","description":"Milk, Cheese, Pizza, Fruit, Tylenol, Beer and Wine","done":true}
#
@app.route('/todo/api/v1.0/tasks/<int:task_id>', methods=['PUT'])
@token_required
def update_task(current_user, task_id):
    print(f"update_task: Valid bearer token for user = {current_user}")
    task = [task for task in tasks if task['id'] == task_id]

    if len(task) == 0:
        abort(404)
    if not request.json:
        abort(400)

    task[0]['title'] = request.json.get('title', task[0]['title'])
    task[0]['description'] = request.json.get('description', task[0]['description'])
    task[0]['done'] = request.json.get('done', task[0]['done'])
    return jsonify({'task': task[0]})

#
# DELETE Method
#
# URL: http://localhost:5000/todo/api/v1.0/tasks/2
#
@app.route('/todo/api/v1.0/tasks/<int:task_id>', methods=['DELETE'])
@token_required
def delete_task(current_user, task_id):
    print(f"delete_task: Valid bearer token for user = {current_user}")
    task = [task for task in tasks if task['id'] == task_id]
    if len(task) == 0:
        abort(404)
    tasks.remove(task[0])
    return jsonify({'result': True})

#
# Login Method using credentials stored in HTTP Basic Auth
#
# URL: http://localhost:5000/todo/api/v1.0/login
#
@app.route('/todo/api/v1.0/login', methods=['POST'])
def login():
    auth_header = request.headers.get('Authorization')

    if not auth_header or not auth_header.startswith('Basic '):
        return jsonify({'message': 'Basic Auth header missing'}), 401

    try:
        # Extract and decode the base64-encoded credentials
        encoded_credentials = auth_header.split(' ')[1]
        decoded_credentials = base64.b64decode(encoded_credentials).decode('utf-8')
        username, password = decoded_credentials.split(':')
    except (IndexError, ValueError):
        return jsonify({'message': 'Invalid Basic Auth format'}), 401

    if username not in users or users[username] != password:
        return jsonify({'message': 'Invalid credentials'}), 401

    payload = {
        'user_id': username,
        'exp': datetime.datetime.now(datetime.timezone.utc) + datetime.timedelta(minutes=30)
    }
    token = jwt.encode(payload, app.config['SECRET_KEY'], algorithm='HS256')
    return jsonify({'token': token})

#
# If this run as startup file, the if statement is true and the main() is called.
# This will run the flask application "app".
#
if __name__ == '__main__':
    app.run(debug=True)

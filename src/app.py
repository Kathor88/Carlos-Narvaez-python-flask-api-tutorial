from flask import Flask, jsonify, request

app = Flask(__name__)

# Global variable with one task object
todos = [ { "label": "My first task", "done": False } ]

@app.route('/todos', methods=['GET'])
def get_todos():
    # Return the global variable jsonified
    return jsonify(todos)

@app.route('/todos', methods=['POST'])
def add_new_todo():
    # 1. Convert request body into a dictionary
    request_body = request.get_json(force=True)
    print("Incoming request with the following body", request_body)
    
    # 2. Add the dictionary into the list of todos
    todos.append(request_body)
    
    # 3. Return the updated list jsonified
    return jsonify(todos)

@app.route('/todos/<int:position>', methods=['DELETE'])
def delete_todo(position):
    # 1. Receive the position as a parameter
    print("This is the position to delete:", position)
    
    # 2. Remove the task from the list using pop
    todos.pop(position)
    
    # 3. Return the updated list jsonified
    return jsonify(todos)

# These two lines should always be at the end of your app.py file
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=3245, debug=True)

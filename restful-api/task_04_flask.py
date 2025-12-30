#!/usr/bin/python3
"""
task_04_flask.py
A simple Flask API with in-memory user storage.
"""

from flask import Flask, jsonify, request

app = Flask(__name__)

# IMPORTANT: Keep this empty for the checker (no test data in repo)
users = {}


@app.route("/", methods=["GET"])
def home():
    return "Welcome to the Flask API!"


@app.route("/status", methods=["GET"])
def status():
    return "OK"


@app.route("/data", methods=["GET"])
def data():
    # Return list of usernames
    return jsonify(list(users.keys()))


@app.route("/users/<username>", methods=["GET"])
def get_user(username):
    user = users.get(username)
    if user is None:
        return jsonify({"error": "User not found"}), 404
    return jsonify(user)


@app.route("/add_user", methods=["POST"])
def add_user():
    # Validate JSON body
    if not request.is_json:
        return jsonify({"error": "Invalid JSON"}), 400

    data_in = request.get_json(silent=True)
    if data_in is None:
        return jsonify({"error": "Invalid JSON"}), 400

    username = data_in.get("username")
    if not username:
        return jsonify({"error": "Username is required"}), 400

    if username in users:
        return jsonify({"error": "Username already exists"}), 409

    # Store the whole object (ensure username exists in stored object)
    user_obj = dict(data_in)
    user_obj["username"] = username
    users[username] = user_obj

    return jsonify({"message": "User added", "user": user_obj}), 201


if __name__ == "__main__":
    # Run on default 127.0.0.1:5000
    app.run()

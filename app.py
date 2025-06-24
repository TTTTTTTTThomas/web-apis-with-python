from flask import Flask, jsonify, request

# Intitialise the app
app = Flask(__name__)

# Define what the app does
@app.get("/greet")
def index():
    """
    TODO:
    1. Capture first name & last name
    2. If either is not provided: respond with an error
    3. If first name is not provided and second name is provided: respond with "Hello Mr <second-name>!"
    4. If first name is provided byt second name is not provided: respond with "Hello, <first-name>!"
    5. If both names are provided: respond with a question, "Is your name <fist-name> <second-name>
    """

    #if name(data) is not passed as query stringm capture it and use it programmetically
    # 1. Capture first name & last name
    fname = request.args.get("first_name")
    lname = request.args.get("last_name")

    # 2. if either is not provided: respond with an error
    if not fname and not lname:
        return jsonify({"status": "error"})
    # 3. If first name is not provided and second name is provided: respond with "Hello Mr <second-name>!"
    elif not frame and lname:
        response = {"data": f"Hello Mr {lname}!"}
    # 4. If first name is provided but second name is not provided
    elif fname and not lname:
        response = {"data": f"Hello, {fname}!"}
    # 5. If both names are provided: respond with a question, "Is your name <first-name> <second-name>?"
    else:
        response = {"data": f"Is your name {fname} {lname}?"}
    name = request.args.get("name")
    return jsonify(response)
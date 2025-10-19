from flask import Flask, jsonify
app = Flask(__name__)

@app.route("/")
def hello_world():
    return "Hello World"

@app.route("/message_dict", methods )
def get_dict():
    result_dict = {"message":"Hello World"}
    return result_dict


@app.route("/dict_json")
def get_dict_json():
    user = {
        "id": 1,
        "name": "Bharath",
        "role": "Engineer"
    }
    return jsonify(user)


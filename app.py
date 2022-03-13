from crypt import methods
from flask import Flask, request
import io
import json
from src.nlu.helpers import NluModel


app = Flask(__name__)

with io.open("./dataset2.json") as f:
    sample_dataset = json.load(f)

nlu_model = NluModel()
nlu_model.fitToData(sample_dataset)


@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"


@app.route("/bot", methods=["POST"])
def handle_bot():
    content = request.get_json()
    message = content.get("message")
    return nlu_model.parse(message)

from flask import Flask, request, jsonify
from datetime import datetime
import re

app = Flask(__name__)

memcache = {}


@app.route("/")
def hello_world():
    return "Hello world!"


@app.route("/hello")
def hello():
    return "Hello!"


@app.route("/hello/<name>")
def hello_there(name):
    now = datetime.now()
    formatted_now = now.strftime("%A, %d %B, %Y at %X")

    # Filter the name argument to letters only using regular expressions. URL arguments
    # can contain arbitraty text, so we restrict to safe characters only.
    match_object = re.match("[a-zA-Z]+", name)

    if match_object:
        clean_name = match_object.group(0)
    else:
        clean_name = "Friend"

    content = "Hello there, " + clean_name + "! It's " + formatted_now
    return content


@app.route("/cache", methods=["GET", "POST"])
def data():
    if request.method == "POST":
        memcache.update(request.json)
        return "Success"
    else:
        return jsonify(memcache)

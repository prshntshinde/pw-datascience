from flask import Flask
from flask import request

app = Flask(__name__)


@app.route("/")
def hello_world():
    return "Hello World!"


@app.route("/hello1")
def hello_world1():
    return "Hello World 1!!!"


@app.route("/sum")
def calculate():
    a = 5 + 6
    return f"This is my first function in flask {a}"

# Parameters


@app.route("/input")
def req_input():
    data = request.args.get('x')
    return f"This is my input from url: {data}"


if __name__ == "__main__":
    app.run(host="127.0.0.1", port=5000)

from flask import Flask
from flask import request
from flask import redirect
from flask import url_for

app = Flask(__name__)


#@app.route("/")
#def hello_world():
#    return "Hello World!"


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

@app.route("/welcome")
def welcome():
    return "Welcome to ABC Corporation."

@app.route("/")
def show_details():
    return "Company Name: ABC Corporation <br> Location: India <br> Contact Detail: 999-999-9999"

# URL Building
@app.route("/admin")
def admin():
    return "<b>Hello Admin</b>. You have access to everything!!!"

@app.route("/guest/<guest>")
def guest(guest):
    """method for guest user
    """
    return f"<b>Hello {guest}</b>. You are a guest and have limited access."

@app.route("/user/<name>")
def user(name):
    if name == 'admin':
        return redirect(url_for("admin"))
    else:
        return redirect(url_for('guest',guest=name))

if __name__ == "__main__":
    app.run(host="127.0.0.1", port=5000)

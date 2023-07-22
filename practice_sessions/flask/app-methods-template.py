from flask import Flask, request, render_template, jsonify

app = Flask(__name__)


@app.route("/")
def home_page():
    return render_template('index.html')
    # return 'Hello'


@app.route("/math", methods=['POST'])
def math_ops():
    if request.method == 'POST':
        ops = request.form['operation']
        num1 = request.form['num1']
        num2 = request.form['num2']
        if ops == 'add':
            r = int(num1) + int(num2)
            result = f'The sum of {num1} and {num2} is {r}'

        if ops == 'sub':
            r = int(num1) - int(num2)
            result = f'The sum of {num1} and {num2} is {r}'

        if ops == 'mul':
            r = int(num1) * int(num2)
            result = f'The sum of {num1} and {num2} is {r}'

        if ops == 'div':
            r = int(num1) / int(num2)
            result = f'The sum of {num1} and {num2} is {r}'

        return render_template('results.html', result=result)


# Postman
@app.route("/postman_action", methods=['POST'])
def math_ops1():
    if request.method == 'POST':
        ops = request.json['operation']
        num1 = request.json['num1']
        num2 = request.json['num2']
        if ops == 'add':
            r = int(num1) + int(num2)
            result = f'The sum of {num1} and {num2} is {r}'

        if ops == 'sub':
            r = int(num1) - int(num2)
            result = f'The sum of {num1} and {num2} is {r}'

        if ops == 'mul':
            r = int(num1) * int(num2)
            result = f'The sum of {num1} and {num2} is {r}'

        if ops == 'div':
            r = int(num1) / int(num2)
            result = f'The sum of {num1} and {num2} is {r}'

        return jsonify(result)


if __name__ == "__main__":
    app.run(host="127.0.0.1", port=5000)

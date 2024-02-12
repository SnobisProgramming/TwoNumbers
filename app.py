from flask import Flask, render_template, request

app = Flask(__name__)


@app.route("/", methods=["POST", "GET"])
def index():  # put application's code here
    return render_template("index.html")


@app.route("/solution", methods=["POST", "GET"])
def wordCount():
    num1 = request.form.get("num1")
    operation = request.form.get("operation")
    num2 = request.form.get("num2")
    if operation == "+":
        result = num1 + num2
    elif operation == "-":
        result = num1 - num2
    elif operation == "*":
        result = num1 * num2
    else:
        try:
            result = num1 / num2
        except ZeroDivisionError:
            return render_template("failure.html")
    return render_template("solution.html", result=result, num1=num1, operation=operation, num2=num2)


if __name__ == '__main__':
    app.run()
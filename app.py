from flask import Flask, render_template, request

app = Flask(__name__)


@app.route("/")
def index():  # put application's code here
    return render_template("index.html")


@app.route("/solution")
def wordCount():
    try:
        num1 = int(request.args.get("num1"))
    except ValueError:
        num1 = 0
    try:
        num2 = int(request.args.get("num2"))
    except ValueError:
        num2 = 0
    operation = request.args.get("operation")

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

    return render_template("solutions.html", result=result, num1=num1, operation=operation, num2=num2)


if __name__ == '__main__':
    app.run()

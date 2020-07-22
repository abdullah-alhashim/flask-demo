from flask import Flask, request

app = Flask(__name__)


@app.route("/")
def index():
    return """
    <form method='post' action='http://localhost:5000/hello'>
        <input id='name' type='text' placeholder='name' name='name'>
        <input type='submit'>
    </form>
    """


@app.route("/hello")
def hello():
    return "Hello"


@app.route("/hello", methods=["post"])
def hello_name():
    name = request.form["name"]
    return f"Hello {name}"


if __name__ == '__main__':
    Flask.run(app)

from flask import Flask

app = Flask(__name__)


@app.route('/')
def hello_world():
    return "hello world!"


@app.route('/aaa')
def hello_earth():
    return "hello earth!"


if __name__ == '__main__':
    app.run()

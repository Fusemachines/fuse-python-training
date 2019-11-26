from flask import Flask, request

app = Flask(__name__)

@app.route("/")
def home():
    params = request.args
    print(params)
    return "This is app page"

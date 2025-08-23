from flask import Flask

app = Flask(__name__)

@app.route("/")
def index():
    return "<p>Hello, Flask!</p>"

# 第二頁
@app.route("/name")
def my_myName():
    return "<h1>Anna</h1>"
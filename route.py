from flask import Flask

app=Flask(__name__)

@app.route("/")
def main():
    return 'Welcome'

@app.route("/about")
def about():
    return 'My Self'
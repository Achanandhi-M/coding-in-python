from flask import Flask
from markupsafe import escape

app=Flask(__name__)

@app.route('/user/<username>')
def showUser(username):
    return f'Welcome! {escape(username)}'

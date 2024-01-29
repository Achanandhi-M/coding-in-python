from flask import Flask

app=Flask(__name__)

@app.route('/projects/')
def projects():
    return 'My projects page'

@app.route('/about')
def about():
    return 'The About page'
from flask import Flask, render_template

app=Flask(__name__)

@app.route('/hello')
def template():
    return render_template('hello.html')
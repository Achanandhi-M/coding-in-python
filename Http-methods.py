from flask import Flask, request

from markupsafe import escape

app=Flask(__name__)

@app.route('/login',methods=['GET','POST'])

def login():
    if request.method == 'POST':
        return do_the_login()
    else:
        return show_the_login_form()


def do_the_login():
    return 'Enter your Credentials'


def show_the_login_form():
    return 'Access the form'
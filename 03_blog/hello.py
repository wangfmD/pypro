from flask import Flask, request, make_response
from flask_script import Manager

app = Flask(__name__)
manager = Manager(app)

@app.route('/')
def index():
    user_agent = request.headers.get('User_Agent')
    for k, v in request.__dict__.items():
        print k, "==", v



    return '<p>U browser is %s</p>' % user_agent

@app.route('/wfm')
def indexwfm():
    response = make_response('<h1>This document carries a cookie!</h1>')
    response.set_cookie('answer', '42')
    return response

@app.route('/user/<name>')
def user(name):
    return '<h1>Hello, %s!</h1>' % name

if __name__ == '__main__':
    manager.run()

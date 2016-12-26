from flask_script import Manager
from app import app
import sqlite3

manager = Manager(app)


@manager.command
def hello():
    print 'hello world'


@manager.option('-m', '--msg', dest='msg_val', default='world')
def hello_world(msg_val):
    print 'hello' + msg_val

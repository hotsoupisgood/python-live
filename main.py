from flask import Flask, render_template, Markup
from util import getHtml, duplicate, displayArray
from flask_socketio import SocketIO, emit
app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret!'
socketio = SocketIO(app)

@app.route('/')
def home():
    return displayArray()
@socketio.on('connect')
def test_connect():
    emit('after connect',  {'data':'Lets dance'})
#@socketio.on('plz reload', namespace='/test')
#def test_message(message):
#    emit('reload', {'data': message['data']})

if __name__ == '__main__':
    socketio.run(app, host='0.0.0.0',port=5001, debug=True)
    print('a;lsdfkj')
    while True:
        print('a;lsdfkj')
        if os.path.getmtime('test.py')<=5:
            test_message('hello')

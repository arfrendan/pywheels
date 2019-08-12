import eventlet
import socketio

sio=socketio.Server()
app = socketio.WSGIApp(sio,static_files={'/':{'content_type':'text/html','filename':'index.html'}})

def connect(sid,environ):
    print('connect',sid)
    
def my_message(sid,data):
    print('message',data)
    
def disconnect(sid):
    print('disconnect',sid)
    
if __name__ == '__main__':
    eventlet.wsgi.server(eventlet.listen(('0.0.0.0',5000)),app)
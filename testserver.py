import http.server
import socketserver
from urllib import parse


class MyHttpRequestHandler(http.server.SimpleHTTPRequestHandler):
    def do_GET(self):

        if self.path == '/':
            self.path = 'index.html'
        elif self.path == '/107839786668602547206046647333321816769962428078371783895815794196481':
            self.path = 'answer.html'

        return http.server.SimpleHTTPRequestHandler.do_GET(self)



# Create an object of the above class
handler_object = MyHttpRequestHandler

PORT = 8000
my_server = socketserver.TCPServer(("", PORT), handler_object)

# Star the server
my_server.serve_forever()
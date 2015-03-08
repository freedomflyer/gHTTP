from Errors import *
import socket
from urlparse import urlparse
from HttpUtils import RequestBuilder

CRLF = "\r\n"
DOUBLE_CRLF = "\r\n\r\n"

class gHTTP:
    def __init__(self):
        self.headers = {}
        self.raw_header_data = ""
        self.raw_body_data = ""

    def get(self, url, port=80):
        self.url = url
        self.port = port

        try:
            self.open_socket()
            self.send_request()
            self.parse_headers()
            self.get_body()
        finally:
            self.sock.close()

    def open_socket(self):
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        url_object = urlparse(self.url)
        ip = socket.gethostbyname(url_object.hostname)
        server_address = (ip, self.port)
        self.sock.connect(server_address)

    def send_request(self):
        rb = RequestBuilder(self.url)
        self.sock.sendall(rb.request)

    def parse_headers(self):
        '''Reads through and parses header information'''
        while True:
            if self.raw_header_data.__contains__(DOUBLE_CRLF):
                break
            self.raw_header_data += self.sock.recv(1)

        # Split raw HTTP Header data into lines
        lines = self.raw_header_data.split(CRLF)

        # Doesn't support redirects yet
        if lines[0].__contains__("302"):
            raise HttpCodeNotSupportedError("302 not supported")

        # Adds each reponse line to reponse header dictionary
        # Skips HTTP status line and last two empty lines
        for line in lines[1:-2]:
            line_parts = line.split(":")
            self.headers[line_parts[0]] = line_parts[1]

    def get_body(self):
        '''Read body data'''
        while len(self.raw_body_data) < int(self.headers['Content-Length']):
            self.raw_body_data += self.sock.recv(1)

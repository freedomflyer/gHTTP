from urlparse import urlparse
import socket

class InvalidRequestError(object):
    pass

DEFAULT_PORT = 80
DEFAULT_HTTP_VERSION = "HTTP/1.1"
DEFAULT_METHOD = "GET"
CRLF = "\r\n"
DOUBLE_CRLF = "\r\n\r\n"

class RequestBuilder:
    def __init__(self, url, method=DEFAULT_METHOD, port=DEFAULT_PORT, http_version=DEFAULT_HTTP_VERSION):
        if method not in ["GET"]:
            raise InvalidRequestError('The request in invalid')

        try:
            url_object = urlparse(url)
        except:
            InvalidRequestError('The request URL in invalid')

        self.url_object = url_object
        self.frag = self.url_object.fragment
        self.method = method
        self.url = url
        self.port = port
        self.http_version = http_version
        self.request_headers = {}
        self.create_request()
        print self.request

    def create_request(self):
        # Build first request line
        self.initial_request_line = "%s %s %s" % (self.method, self.url_object.path, self.http_version)

        # Get host IP information
        self.request_ip_address = socket.gethostbyname(self.url_object.hostname)
        self.request_headers["Host"] = self.url_object.hostname

        # Build Request String
        self.request = self.initial_request_line + CRLF
        for header in self.request_headers:
            self.request += "%s: %s%s" % (header, self.request_headers[header], CRLF)

        # Terminating double carriage return + line feed
        self.request += DOUBLE_CRLF













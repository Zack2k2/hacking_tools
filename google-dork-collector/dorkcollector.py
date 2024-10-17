#!/usr/bin/python3
import http.server
import socketserver

# Define a custom handler to process incoming POST requests
class MyHandler(http.server.BaseHTTPRequestHandler):
    def log_message(self, format, *args):
        # Override the log_message method to suppress access logs
        pass    
    def do_POST(self):
        content_length = int(self.headers['Content-Length'])
        data = self.rfile.read(content_length).decode('utf-8')
        self.send_response(200)
        self.end_headers()
        response = f"{data}"
        if not (response.startswith("http://www.google") or response.startswith("https://www.google") or ("google.com" in response)):
            print(response);
        #self.wfile.write(response.encode('utf-8'))

# Create an HTTP server that listens on port 8080
with socketserver.TCPServer(("", 65535), MyHandler) as httpd:
    httpd.serve_forever()


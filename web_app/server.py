
import http.server
import socketserver
import os

PORT = 8000
PROJECT_ROOT = "H:/Google Drive/MN_SprinklerFitters_Exam"

class MyHandler(http.server.SimpleHTTPRequestHandler):
    def translate_path(self, path):
        # Get the original path requested by the client
        original_path = path

        # If the request is for the root, serve index.html from templates
        if original_path == '/':
            path = os.path.join(PROJECT_ROOT, 'web_app', 'templates', 'index.html')
        # If the request is for mindmap_data.json, serve it from the project root
        elif original_path == '/mindmap_data.json':
            path = os.path.join(PROJECT_ROOT, 'mindmap_data.json')
        # For all other requests, serve relative to the project root
        else:
            path = os.path.join(PROJECT_ROOT, path.lstrip('/'))

        return path

Handler = MyHandler

with socketserver.TCPServer(("", PORT), Handler) as httpd:
    print(f"serving at port {PORT}")
    print(f"You can access the mind map at http://localhost:{PORT}")
    httpd.serve_forever()

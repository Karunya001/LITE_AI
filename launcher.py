import os
import sys
import webbrowser
import subprocess
import threading
import http.server
import socketserver

# Detect base path (works for exe and normal Python run)
if getattr(sys, 'frozen', False):
    base_path = sys._MEIPASS
else:
    base_path = os.path.dirname(os.path.abspath(__file__))

frontend_path = os.path.join(base_path, "frontend")
PORT = 8000

# Start simple HTTP server in background for frontend
def start_server():
    os.chdir(frontend_path)
    handler = http.server.SimpleHTTPRequestHandler
    with socketserver.TCPServer(("", PORT), handler) as httpd:
        print(f"🚀 Serving frontend at http://localhost:{PORT}")
        httpd.serve_forever()

server_thread = threading.Thread(target=start_server, daemon=True)
server_thread.start()

# Start all backend app scripts on different ports
backend_scripts = [
    ("app1.py", "8501"),
    ("app2.py", "8502"),
    ("app3.py", "8503"),
    ("app4.py", "8504"),
    ("app5.py", "8505"),
]

for script, port in backend_scripts:
    script_path = os.path.join(base_path, script)
    if os.path.exists(script_path):
        subprocess.Popen([sys.executable, script_path, f"--server.port={port}"])
        print(f"✅ Started {script} on port {port}")

# Open browser to dashboard
webbrowser.open(f"http://localhost:{PORT}/index.html")

# Keep launcher alive
try:
    while True:
        pass
except KeyboardInterrupt:
    print("\nServer stopped.")

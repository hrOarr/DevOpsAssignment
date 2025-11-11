from flask import Flask
import socket
import os

app = Flask(__name__)
COMMIT = os.environ.get("APP_COMMIT", "unknown")

@app.route("/")
def index():
    return f"Hostname: {socket.gethostname()}<br>Commit: {COMMIT}\n"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
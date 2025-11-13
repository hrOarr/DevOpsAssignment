from flask import Flask, render_template_string
import socket
import os

app = Flask(__name__)

COMMIT = os.environ.get("APP_COMMIT", "unknown")
HOSTNAME = socket.gethostname()

TEMPLATE = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Deployment Info</title>
    <style>
        body {
            font-family: "Segoe UI", Roboto, Helvetica, Arial, sans-serif;
            background: linear-gradient(135deg, #74ABE2, #5563DE);
            color: #fff;
            text-align: center;
            padding: 60px 20px;
            margin: 0;
            height: 100vh;
            display: flex;
            flex-direction: column;
            justify-content: center;
        }
        .card {
            background: rgba(255, 255, 255, 0.1);
            border-radius: 16px;
            padding: 40px;
            max-width: 500px;
            margin: auto;
            box-shadow: 0 4px 30px rgba(0,0,0,0.2);
            backdrop-filter: blur(8px);
        }
        h1 {
            margin-bottom: 10px;
            font-size: 2.2em;
        }
        .info {
            font-size: 1.2em;
            line-height: 1.6;
        }
        .label {
            font-weight: bold;
            color: #FFD700;
        }
        footer {
            position: fixed;
            bottom: 15px;
            width: 100%;
            text-align: center;
            font-size: 0.9em;
            opacity: 0.8;
        }
    </style>
</head>
<body>
    <div class="card">
        <h1>🚀 Web App Deployment Info</h1>
        <div class="info">
            <p><span class="label">Hostname:</span> {{ hostname }}</p>
            <p><span class="label">Commit:</span> {{ commit }}</p>
        </div>
    </div>
    <footer>
        &copy; {{ year }} Simple Deployment Demo
    </footer>
</body>
</html>
"""

@app.route("/")
def index():
    from datetime import datetime
    return render_template_string(TEMPLATE,
                                  hostname=HOSTNAME,
                                  commit=COMMIT,
                                  year=datetime.now().year)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)

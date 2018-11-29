from flask import Flask
import os
import socket

app = Flask(__name__)

@app.route("/")
def hello():
    html = "<h3>Hello {name}! This is a Test App</h3>" \
           "<b>Running at:</b> {hostname}<br/>"
    return html.format(name="World", hostname=socket.gethostname())

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=80)


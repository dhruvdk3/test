from flask import Flask
import os
import subprocess
import datetime

app = Flask(__name__)

@app.route('/htop')
def htop():
    return "Hello, Flask is working!"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000)
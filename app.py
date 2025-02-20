from flask import Flask
import os
import subprocess
import pytz
from datetime import datetime

app = Flask(__name__)

@app.route("/htop")
def htop():
    username = os.getenv("USER") or os.getenv("USERNAME")
    ist = pytz.timezone("Asia/Kolkata")
    server_time = datetime.now(ist).strftime("%Y-%m-%d %H:%M:%S %Z")
    top_output = subprocess.getoutput("top -bn1 | head -20")
    
    return f"""
    <pre>
    Name - Dhruv Kumawat
    Username - {username}
    Server Time in IST - {server_time}
    Top Output:
    {top_output}
    </pre>
    """

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
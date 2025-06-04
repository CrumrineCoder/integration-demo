import requests 
from flask import Flask

app = Flask(__name__)

@app.route("/trigger")
def trigger():
    r = requests.get("http://service-b:5001/respond")
    return f"Service B Said: {r.text}", 200

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
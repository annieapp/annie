from datetime import datetime, timedelta
from flask import Flask

app = Flask(__name__)


@app.route("/status", methods=["GET", "POST"])
def status():
    return "{'status':'analytics server online'}"


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=2000)

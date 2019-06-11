from datetime import datetime, timedelta
from flask import Flask

app = Flask(__name__)


@app.route("/", methods=["GET"])
def base():
    return "{'status':'analytics server online'}"


@app.route("/ping", methods=["GET", "POST"])
def ping():
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    log = open("joins.log", "a")
    log.write(str(timestamp) + "\n")
    log.close()

    total = int(open("total.log", "r").readline().rstrip())
    open("total.log", "w").write(str(total + 1))

    return "{'status':'true'}"


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=2000)

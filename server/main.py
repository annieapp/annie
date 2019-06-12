from random import randint
from datetime import datetime
from flask import Flask
from filehandlers import AbstractFile, FileHandler
import json
import logging
import sys

app = Flask(__name__)

keysfile = FileHandler(AbstractFile("tokens.cfg"))


@app.route("/", methods=["GET"])
def base():
    return json.dumps({
        'status': 'analytics server online'
    })


@app.route("/keys/new", methods=["GET", "POST"])
def new_key():
    genkey = ""
    while True:
        genkey = str(randint(10, 100000000))
        cache = []
        for i, p in enumerate(keysfile.get_cache()):
            cache.append(keysfile.get_cache()[i].replace("\n", ""))
        if genkey in cache:
            continue
        else:
            break
    keysfile.get_file().wrap().write(genkey)
    keysfile.refresh()
    return json.dumps({
        'result': {
            'key': genkey,
            'message': 'you are now ready to use the Annie API'
        }
    })


@app.route("/ping", methods=["GET", "POST"])
def ping():
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    log = open("joins.log", "a")
    log.write(str(timestamp) + "\n")
    log.close()

    total = int(open("total.log", "r").readline().rstrip())
    open("total.log", "w").write(str(total + 1))

    return json.dumps({
        'status': 'worked'
    })


app.logger.setLevel(logging.DEBUG)
app.logger.addHandler(logging.FileHandler(filename='annie_backend.log', encoding='utf-8', mode='w'))
app.logger.addHandler(logging.StreamHandler(sys.stdout))

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=2000)

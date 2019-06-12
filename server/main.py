"""
Annie Modified MIT License

Copyright (c) 2019-present year Reece Dunham and the Annie Team

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, and/or distribute
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE. SELLING THE SOFTWARE IS ALSO NOT ALLOWED WITHOUT WRITTEN PERMISSION
FROM THE ANNIE TEAM.
"""

from random import randint
from datetime import datetime
from flask import Flask
from lcbools import true, false
from filehandlers import AbstractFile, FileHandler
from . import config as opts
import json
import logging
import sys

app = Flask(__name__)

if opts.verbose:
    app.logger.setLevel(logging.DEBUG)
    app.logger.addHandler(logging.StreamHandler(sys.stdout))
app.logger.addHandler(logging.FileHandler(filename='annie_backend.log', encoding='utf-8', mode='w'))

keysfile = FileHandler(AbstractFile("tokens.cfg"))


@app.route("/", methods=["GET"])
def base():
    return json.dumps({
        'status': 'analytics server online'
    })


@app.route("/keys/new", methods=["GET", "POST"])
def new_key():
    if opts.manual_keygen:
        return json.dumps({
            'result': {
                'fail': true
            },
            'message': 'the owner of this Annie server has disabled automatic key signups - if you are the owner, check your config.py'
        })
    genkey = ""
    keyprivate = ""
    while True:
        genkey = str(randint(10, 100000000))
        keyprivate = str(randint(10, 100000000))
        cache = []
        for i, p in enumerate(keysfile.get_cache()):
            cache.append(keysfile.get_cache()[i].replace("\n", "").split("|"))
        if genkey in cache or keyprivate in cache:
            continue
        else:
            break
    keysfile.get_file().wrap().write(f"{genkey}|{keyprivate}")
    keysfile.refresh()
    return json.dumps({
        'result': {
            'fail': false,
            'auth': {
                'key': genkey,
                'private-key': keyprivate
            },
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


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=2000)

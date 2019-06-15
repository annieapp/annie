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

from datetime import datetime
from flask import Flask, render_template, request, Response
from lcbools import true, false
from filehandlers import AbstractFile, FileHandler
import config as opts
import random
import json
import logging
import sys
import string

app = Flask(__name__)

if opts.verbose:
    app.logger.setLevel(logging.DEBUG)
    app.logger.addHandler(logging.StreamHandler(sys.stdout))
app.logger.addHandler(logging.FileHandler(filename='annie_backend.log', encoding='utf-8', mode='w'))

keysfile = FileHandler(AbstractFile("tokens.cfg"))


def genkey():
    return ''.join(random.choice(string.ascii_letters + string.digits) for _ in range(15))


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
            'message': 'the owner of this Annie server has disabled automatic key signups in the config.py'
        })
    genkey = ""
    keyprivate = ""
    while True:
        genkey = str(genkey())
        keyprivate = str(genkey())
        cache = []
        for i, p in enumerate(keysfile.get_cache()):
            cache.append(keysfile.get_cache()[i].replace("\n", "").split("|"))
        if genkey in cache or keyprivate in cache:
            continue
        else:
            break
    keysfile.get_file().wrap().write(f"{genkey}|{keyprivate}\n")
    keysfile.refresh()
    return json.dumps({
        'result': {
            'fail': false,
            'auth': {
                'key': genkey,
                'private-key': keyprivate
            }
        }
    })


@app.route("/connect", methods=["GET", "POST"])
def connect():
    try:
        with open('stats.info') as f:
            data = json.load(f)
        key = request.args.get("key", type = str)
        data[key][0] = data[key][0] + 1
        with open('stats.info', 'w') as w:
            json.dump(data, w)
    except:
        return Response(
            json.dumps({
                'result': {
                    'fail': true
                },
                "message": 'Invalid or missing API key'
            }),
            mimetype='application/json'
        )

    return Response(
        json.dumps({
            'result': {
                'fail': false
            }
        }),
        mimetype='application/json'
    )


@app.route("/stats", methods=["GET", "POST"])
def stats():
    try:
        with open('stats.info') as f:
            data = json.load(f)
        key = request.args.get("key", type=str)
        private = request.args.get("private", type=str)
        if data[key][1] == private:
            return Response(
                json.dumps({
                    'result' {
                        'fail': false,
                        'connections': data[key][0]
                    }
                }),
                mimetype='application/json'
            )
        return Response(
            json.dumps({
                'result': {
                    'fail': true,
                    'message': 'Invalid or missing Private Key'
                }
            }),
            mimetype='application/json'
        )
    except:
        return Response(
            json.dumps({
                "status": "false",
                "message":"Invalid or missing API Key"
            }),
            mimetype='application/json')


@app.errorhandler(404)
def page_not_found(error):
    return render_template(
        "error.html",
        code="404",
        desc="Oh no, looks like we couldn't find the page you are looking for."
    ), 404


@app.errorhandler(500)
def internal_server_exception(error):
    return render_template(
        "error.html",
        code="500",
        desc="Oh no, there was an error on our end. Please try again later."
    ), 500


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=opts.dev_port)

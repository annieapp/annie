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
import config as opts
import random
import json
import logging
import sys
import string

ico_base64 = "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"

app = Flask(__name__)

if opts.verbose:
    app.logger.setLevel(logging.DEBUG)
    app.logger.addHandler(logging.StreamHandler(sys.stdout))
app.logger.addHandler(logging.FileHandler(filename='annie_backend.log', encoding='utf-8', mode='w'))


def genkey():
    return ''.join(random.choice(string.ascii_letters + string.digits) for _ in range(15))


@app.route("/", methods=["GET"])
def base():
    return Response(
        json.dumps({
            "status": "analytics server online"
        }),
        mimetype='application/json'
    )


@app.route("/keys/new", methods=["GET", "POST"])
def new_key():
    if opts.manual_keygen:
        return json.dumps({
            "result": {
                "fail": true
            },
            "message": "the owner of this Annie server has disabled easy key signups in the config.py"
        })

    with open('stats.info') as f:
        data = json.load(f)

    key = generateKey()
    private = generateKey()
    data[key] = (0, private)

    with open('stats.info', 'w') as w:
        json.dump(data, w)

    return Response(
        json.dumps({
            "result": {
                "fail": false,
                "auth": {
                    "key": key,
                    "private-key": private
                }
            }
        }),
        mimetype='application/json'
    )


@app.route("/connect", methods=["GET", "POST"])
def connect():
    try:
        with open('stats.info') as f:
            data = json.load(f)
        key = request.args.get("key", type=str)
        data[key][0] = data[key][0] + 1
        with open('stats.info', 'w') as w:
            json.dump(data, w)
    except:
        return Response(
            json.dumps({
                "result": {
                    "fail": true
                },
                "message": "Invalid or missing API key"
            }),
            mimetype='application/json'
        )

    return Response(
        json.dumps({
            "result": {
                "fail": false
            }
        }),
        mimetype='application/json'
    )


@app.route("/stats.json", methods=["GET", "POST"])
def stats():
    try:
        with open('stats.info') as f:
            data = json.load(f)
        key = request.args.get("key", type=str)
        private = request.args.get("private", type=str)
        if data[key][1] == private:
            return Response(
                json.dumps({
                    "result": {
                        "fail": false,
                        "connections": data[key][0]
                    }
                }),
                mimetype='application/json'
            )
        return Response(
            json.dumps({
                "result": {
                    "fail": true,
                    "message": "Invalid or missing private key"
                }
            }),
            mimetype='application/json'
        )
    except:
        return Response(
            json.dumps({
                "result": {
                    "fail": true,
                    "message": "Invalid or missing public key"
                }
            }),
            mimetype='application/json'
        )


@app.route("/favicon.ico")
def favicon():
    return Response(
        ico_base64,
        mimetype='image/x-icon'
    )


@app.errorhandler(403)
def access_denied(error):
    return render_template(
        "error.html",
        code="403",
        desc="Oh no, looks like you don't have permission to do that."
    ), 403


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

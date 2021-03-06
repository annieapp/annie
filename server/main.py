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
import random
import json
import logging
import sys
import os
import string

app = Flask(__name__)

if os.getenv("CI") is None:
    app.logger.setLevel(logging.DEBUG)
    app.logger.addHandler(logging.StreamHandler(sys.stdout))
app.logger.addHandler(logging.FileHandler(filename='annie_backend.log', encoding='utf-8', mode='w'))


def public_key_error():
    """
    Method to get common response for public key errors.

    :return: the flask.Response object
    :rtype flask.Response:
    """
    return Response(
        json.dumps({
            "result": {
                "fail": true,
                "message": "Invalid or missing public key"
            }
        }),
        mimetype='application/json'
    )


def private_key_error():
    """
    Method to get common response for private key errors.

    :return: the flask.Response object
    :rtype flask.Response:
    """
    return Response(
        json.dumps({
            "result": {
                "fail": true,
                "message": "Invalid or missing private key"
            }
        }),
        mimetype='application/json'
    )


def genkey():
    """
    Generate new random API key

    :return: key
    :rtype str:
    """
    return ''.join(random.choice(string.ascii_letters + string.digits) for _ in range(15))


@app.route("/", methods=["GET"])
def base():
    """
    Basic status endpoint.
    """
    return Response(
        json.dumps({
            "status": "analytics server online"
        }),
        mimetype='application/json'
    )


@app.route("/robots.txt", methods=["GET"])
def disallow_search_engine_crawling():
    """
    Prevents common search engines from crawling the server.
    """
    return Response(
        render_template("robots.txt"),
        mimetype="text/plain"
    )


@app.route("/keys/new", methods=["GET", "POST"])
def new_key():
    """
    Get a new key.
    """
    with open('stats.info') as f:
        data = json.load(f)

    key = genkey()
    private = genkey()
    data[key] = (0, private, "")

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


@app.route("/keys/delete", methods=["GET", "POST"])
def delkey():
    """
    Delete a key

    :param key: public key
    :param private: private key
    """
    with open("stats.info", "r") as f:
        data = json.load(f)
    thekey = request.args.get("key", type=str)
    privatekey = request.args.get("private", type=str)
    try:
        if data[thekey][1] == privatekey:
            # private key checks out
            data.pop(thekey)
            with open('stats.info', 'w') as w:
                json.dump(data, w)
            return Response(
                json.dumps({
                    "result": {
                        "fail": false
                    }
                }),
                mimetype='application/json'
            )
        else:
            return private_key_error()
    except KeyError:
        return public_key_error()


@app.route("/connect", methods=["GET", "POST"])
def connect():
    """
    Log a connection to a keyset.

    :param key: the public key
    """
    try:
        with open('stats.info') as f:
            data = json.load(f)
        key = request.args.get("key", type=str)
        data[key][0] = data[key][0] + 1
        data[key][2] = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        with open('stats.info', 'w') as w:
            json.dump(data, w)
    except:
        return public_key_error()

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
    """
    Stats as a JSON endpoint.

    :param key: public key
    :param private: private key
    """
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
                        "connections": data[key][0],
                        "last-join": data[key][2]
                    }
                }),
                mimetype='application/json'
            )
        return private_key_error()
    except:
        return public_key_error()


@app.errorhandler(403)
def access_denied(error):
    """
    Called upon 403 error.
    """
    return render_template(
        "error.html",
        code="403",
        desc="Oh no, looks like you don't have permission to do that."
    ), 403


@app.errorhandler(401)
def access_denied_secondary(error):
    """
    Called upon 401 error.
    """
    return render_template(
        "error.html",
        code="401",
        desc="Oh no, looks like you don't have permission to do that."
    ), 401


@app.errorhandler(404)
def page_not_found(error):
    """
    Called upon 404 error.
    """
    return render_template(
        "error.html",
        code="404",
        desc="Oh no, looks like we couldn't find the page you are looking for."
    ), 404


@app.errorhandler(500)
def internal_server_exception(error):
    """
    Called upon 500 error.
    """
    return render_template(
        "error.html",
        code="500",
        desc="Oh no, there was an error on our end. Please try again later."
    ), 500


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=2000)

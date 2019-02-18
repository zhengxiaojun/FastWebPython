# -*- coding: utf-8 -*-

from fe import app
from flask import render_template, request, Response
from .common import *
import json


def Response_headers(content):
    resp = Response(content)
    resp.headers['Access-Control-Allow-Origin'] = '*'
    return resp


@app.route('/')
@app.route('/index', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        code = request.values.get('code', '')
        # code = request.form['code']
        if code == None or code == "":
            jsondata = {
                "output": "请输入代码",
                "status": "Success",
                "version": get_version()
            }
            jsondata = jsonify(jsondata)
        else:
            jsondata = main(code.encode('utf-8'))

        return jsondata

    return render_template('index.html', title=u'Python在线运行')


@app.errorhandler(403)
def page_not_found(error):
    content = json.dumps({"error_code": "403"})
    resp = Response_headers(content)
    return resp


@app.errorhandler(404)
def page_not_found(error):
    content = json.dumps({"error_code": "404"})
    resp = Response_headers(content)
    return resp


@app.errorhandler(400)
def page_not_found(error):
    content = json.dumps({"error_code": "400"})
    resp = Response_headers(content)
    return resp


@app.errorhandler(405)
def page_not_found(error):
    content = json.dumps({"error_code": "405"})
    resp = Response_headers(content)
    return resp


@app.errorhandler(410)
def page_not_found(error):
    content = json.dumps({"error_code": "410"})
    resp = Response_headers(content)
    return resp


@app.errorhandler(500)
def page_not_found(error):
    content = json.dumps({"error_code": "500"})
    resp = Response_headers(content)
    return resp


if __name__ == '__main__':
    pass

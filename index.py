#!/usr/bin/env python3
# -*- coding: UTF-8 -*-

import requests
import json
from flask import Flask, render_template, url_for, jsonify, request

app = Flask(__name__)


@app.route('/robot')
def robot():
    baseCss = url_for('static', filename='css/robot.css')
    return render_template('robot.html', css=baseCss)


@app.route('/api', methods=['POST'])
def api():
    req = json.loads(str(request.data, encoding="utf-8"))
    headers = {'Content-Type': 'application/json'}
    payload = {
        'perception': {
            "inputText": {
                "text": req['text']
            }
        },
        'userInfo': {
            'apiKey': '87b16acac3b049b6978191db097238b4',
            'userId': '317853'
        }
    }
    r = requests.post(
        "http://openapi.tuling123.com/openapi/api/v2",
        headers=headers,
        data=json.dumps(payload))

    return jsonify(r.json())


if __name__ == '__main__':
    app.config.from_object('flaskCfg')
    app.run()

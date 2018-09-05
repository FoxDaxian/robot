#!/usr/bin/env python3
# -*- coding: UTF-8 -*-

import requests
from flask import Flask, render_template, url_for, jsonify

app = Flask(__name__)


@app.route('/robot')
def robot():
    baseCss = url_for('static', filename='css/robot.css')
    return render_template('robot.html', css=baseCss)


@app.route('/api')
def api():
    payload = {
        'perception': {
            "inputText": {
                "text": "附近的酒店"
            }
        },
        'userInfo': {
            'apiKey': '87b16acac3b049b6978191db097238b4',
            'userId': '317853'
        }
    }
    r = requests.post(
        "http://openapi.tuling123.com/openapi/api/v2", data=payload)
    print(r.text)
    return jsonify({'status': 1, 'data': {'name': '12'}})


if __name__ == '__main__':
    app.config.from_object('flaskCfg')
    app.run()

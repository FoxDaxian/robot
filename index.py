#!/usr/bin/env python3
# -*- coding: UTF-8 -*-

# import requests

# payload = {'perception': {}, 'userInfo': {
#     'apiKey': '87b16acac3b049b6978191db097238b4',
#     'userId': '317853'
# }}

# r = requests.post("http://openapi.tuling123.com/openapi/api/v2", data=payload)
# print(r.text)

from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello():
    return '你123好啊'

if __name__ == '__main__':
    app.config.from_object('flaskCfg')
    app.run()
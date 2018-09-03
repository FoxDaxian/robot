#!/usr/bin/env python3
# -*- coding: UTF-8 -*-

# import requests

# payload = {'perception': {}, 'userInfo': {
#     'apiKey': '87b16acac3b049b6978191db097238b4',
#     'userId': '317853'
# }}

# r = requests.post("http://openapi.tuling123.com/openapi/api/v2", data=payload)
# print(r.text)

from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def hello():
    return render_template('test.html', name='12冯世雨')


@app.route('/user/<name>')
def showUserName(name):
    return '用户名: %s' % name


if __name__ == '__main__':
    app.config.from_object('flaskCfg')
    app.run()

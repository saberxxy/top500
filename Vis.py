#-*- coding=utf-8 -*-
# 使用flask进行可视化

from flask import Flask
from flask import request
from flask import render_template
from flask import Response
import json

import AnaTop500 as at


app = Flask(__name__)

def Response_headers(content):
    resp = Response(content)
    resp.headers['Access-Control-Allow-Origin'] = '*'
    return resp

@app.route('/', methods=['GET', 'POST'])
def home():
    return render_template('home.html')

# 显示国家保有量
@app.route('/echarts')
def echarts():
    cursor = at.getConfig()
    data = at.computerOfCountry(cursor)
    datas = {
        "data":data
        #  "data":[
        #     {"country":"allpe","number":100},
        #     {"country":"peach","number":123},
        #     {"country":"Pear","number":234},
        #     {"country":"avocado","number":20},
        #     {"country":"cantaloupe","number":1},
        #     {"country":"Banana","number":77},
        #     {"country":"Grape","number":43},
        #     {"country":"apricot","number":0}
        # ]
    }
    content = json.dumps(datas)
    resp = Response_headers(content)
    return resp

@app.route('/signin', methods=['GET'])
def signin_form():
    return render_template('form.html')

@app.route('/signin', methods=['POST'])
def signin():
    username = request.form['username']
    password = request.form['password']
    if username=='admin' and  password=='password':
        return render_template('signin-ok.html', username=username)
    return render_template('form.html', message='Bad username or password', username=username)

if __name__ == '__main__':
    app.run(debug=True)
#-*- coding=utf-8 -*-
# 使用flask进行可视化

from flask import Flask
from flask import request
from flask import render_template
from flask import Response
import json

import AnaTop500 as at
import GetOracleConn as goc


app = Flask(__name__)

# 跨域访问
def Response_headers(content):
    resp = Response(content)
    resp.headers['Access-Control-Allow-Origin'] = '*'
    return resp

@app.route('/', methods=['GET', 'POST'])
def home():
    return render_template('home.html')

# 国家保有量页面
@app.route('/number', methods=['GET', 'POST'])
def number():
    return render_template('top500_1.html')

# 国家最高排名页面
@app.route('/rank', methods=['GET', 'POST'])
def rank():
    return render_template('top500_2.html')

# 显示国家保有量
@app.route('/echarts1')
def echarts1():
    cursor = goc.getConfig()
    data = at.computerOfCountry(cursor)
    datas = {
        "data":data
    }
    content = json.dumps(datas)
    resp = Response_headers(content)
    return resp

# 获取各国最大排名
@app.route('/echarts2')
def echarts2():
    cursor = goc.getConfig()
    data = at.maxRank(cursor)
    datas = {
        "data":data
    }
    content = json.dumps(datas)
    resp = Response_headers(content)
    return resp

if __name__ == '__main__':
    app.run(debug=True)
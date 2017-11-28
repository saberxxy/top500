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

# 平均每核计算能力页面
@app.route('/avg', methods=['GET', 'POST'])
def avg():
    return render_template('top500_3.html')

# 计算能力与功耗关系页面
@app.route('/power', methods=['GET', 'POST'])
def power():
    return render_template('top500_4.html')

# 实际计算能力与理论计算能力的差距页面
@app.route('/rr', methods=['GET', 'POST'])
def rr():
    return render_template('top500_5.html')

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

# 平均每核计算能力
@app.route('/echarts3')
def echarts3():
    cursor = goc.getConfig()
    data = at.avgCore(cursor)
    datas = {
        "data":data
    }
    content = json.dumps(datas)
    resp = Response_headers(content)
    return resp

# 计算能力与功耗的关系
@app.route('/echarts4')
def echarts4():
    cursor = goc.getConfig()
    data = at.cpPower(cursor)
    datas = {
        "data":data
    }
    content = json.dumps(datas)
    resp = Response_headers(content)
    return resp

# 实际计算能力与理论计算能力的差距
@app.route('/echarts5')
def echarts5():
    cursor = goc.getConfig()
    data = at.rmaxRpeak(cursor)
    datas = {
        "data":data
    }
    content = json.dumps(datas)
    resp = Response_headers(content)
    return resp


if __name__ == '__main__':
    app.run(debug=True)
    # app.run(host='0.0.0.0')
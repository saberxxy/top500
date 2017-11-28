
# 分析top500超级计算机

"""
1、超级计算机的国家保有量
2、拥有超级计算机的国家所拥有的最好的计算机的最高的排名
3、超级计算机平均每核的计算能力（实际最大性能Rmax）
4、计算能力与功耗的关系
5、实际计算能力与理论计算能力的差距
"""

import pandas as pd
import numpy as np
import cx_Oracle as cxo
import configparser
import matplotlib.pyplot as plt

import GetOracleConn as goc

# 数据入库
def inputDB(cursor):
    df = pd.read_excel('SupercomputerTop500.xlsx', encoding='utf-8')
    # 处理缺失值
    df = df.fillna(0)
    dfLen = len(df)
    # print (df['Rmax'])
    for k in range(0, dfLen):
        df2 = df[k:k + 1]
        # print(type(df2['Cores']))
        cursor.execute("insert into top500 values(:rank, :site, :country, :name, :cpu, :org, :cores, "
                   ":rmax, :rpeak, :power)" , (
            str(list(df2['Rank'])[0]), str(list(df2['Site'])[0]), str(list(df2['Country'])[0]),
            str(list(df2['Name'])[0]), str(list(df2['CPU'])[0]), str(list(df2['Org'])[0]),
            str(list(df2['Cores'])[0]),
            round(float(df2['Rmax']), 3), round(float(df2['Rpeak']), 3), round(float(df2['Power']), 3)
        ))
        cursor.execute("commit")
        print('一条记录入库完毕')

# 分析国家保有量
def computerOfCountry(cursor):
    country = []
    number = []
    sql = "select country, count(1) a from top500 group by country order by a desc"
    for x in cursor.execute(sql).fetchall():
        country.append(x[0])
        number.append(x[1])
    # 处理为前台可接受的格式
    dict1 = dict(zip(country, number))
    data = []
    for c, n in dict1.items():
        a = {}
        a['country'] = c
        a['number'] = n
        data.append(a)
    return data

# 获取最大排名
def maxRank(cursor):
    country = []
    rank = []
    sql = "select country, min(rank) from top500 group by country"
    for x in cursor.execute(sql).fetchall():
        country.append(x[0])
        rank.append(x[1])
    # 处理为前台可接受的格式
    dict1 = dict(zip(country, rank))
    data = []
    for c, n in dict1.items():
        a = {}
        a['country'] = c
        a['rank'] = n
        data.append(a)
    return data

# 平均每核的计算能力
def avgCore(cursor):
    rank = []
    name = []
    country = []
    avgcore = []
    sql = "select rank, name, country, round(rmax/cores, 6) avgcore from top500 order by avgcore desc"
    for x in cursor.execute(sql).fetchall():
        rank.append(x[0])
        name.append(x[1])
        country.append(x[2])
        avgcore.append(x[3])
    # 处理为前台可接受的格式
    tp1 = zip(rank, name, country, avgcore)
    # print(dict1)
    data = []
    for i in tp1:
        # print(i[0])
        a = {}
        a['rank'] = i[0]
        a['name'] = i[1]
        a['country'] = i[2]
        a['avgcore'] = i[3]
        data.append(a)
    return data

# 计算能力与功耗的关系
def cpPower(cursor):
    rmax = []
    power = []
    sql = "select rmax, power from top500 order by power desc"
    for x in cursor.execute(sql).fetchall():
        rmax.append(x[0])
        power.append(x[1])
    # 处理为前台可接受的格式
    dict1 = dict(zip(rmax, power))
    data = []
    for c, n in dict1.items():
        a = {}
        a['rmax'] = c
        a['power'] = n
        data.append(a)
    return data

# 实际计算能力与理论计算能力的差距
def rmaxRpeak(cursor):
    rank = []
    name = []
    country = []
    rR = []
    sql = "select rank, name, country, round(rmax/rpeak, 4) a from top500 order by a desc"
    for x in cursor.execute(sql).fetchall():
        rank.append(x[0])
        name.append(x[1])
        country.append(x[2])
        rR.append(x[3])
    tp1 = zip(rank, name, country, rR)
    data = []
    for i in tp1:
        # print(i[0])
        a = {}
        a['rank'] = i[0]
        a['name'] = i[1]
        a['country'] = i[2]
        a['rR'] = i[3]
        data.append(a)
    return data


def main():
    cursor = goc.getConfig()
    # 数据入库
    # inputDB(cursor)
    # 分析国家保有量
    # a = computerOfCountry(cursor)
    # 分析国家最高排名
    # country, rank = maxRank(cursor)
    # 每核平均计算能力
    # data = avgCore(cursor)

    # 计算能力与功耗的关系
    # data = cpPower(cursor)

    # 实际计算能力与理论计算能力的差距
    data = rmaxRpeak(cursor)
    print(data)
    # print(rank, name, country, rR)


if __name__ == '__main__':
    # a = ['A', 'B', 'C']
    # b = [1, 2, 3]
    # c = []
    # flag = dict(zip(a, b))
    # for t1, t2 in flag.items():
    #     tmp = {}
    #     tmp['name'] = t1
    #     tmp['number'] = t2
    #     c.append(tmp)
    # print(c)

    main()
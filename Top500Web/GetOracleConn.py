# -*- coding=utf-8 -*-
# 获取Oralce连接

import cx_Oracle as cxo

def getConfig():
    oracleHost = '127.0.0.1'
    oraclePort = 1521
    oracleUser = 'scott'
    oraclePassword = 'tiger'
    oracleDatabaseName = 'orcl'
    oracleConn = oracleUser + '/' + oraclePassword + '@' + oracleHost + '/' + oracleDatabaseName
    conn = cxo.connect(oracleConn)
    cursor = conn.cursor()
    print("已获取数据库连接")
    return cursor

if __name__ == '__main__':
    main()

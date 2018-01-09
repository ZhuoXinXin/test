# coding:utf-8

from methods.db import *

def select_table(table,column, condition,value):
    sql = r"select {} from {} where {} = '{}'".format(column,table,condition,value)
    cur.execute(sql)  # 执行sql语句

    lines = cur.fetchall()  # 输出查询结果
    return lines
def select_columns(table,column):
    sql = r"select {} from {}".format(column,table)
    cur.execute(sql)  # 执行sql语句
    lines = cur.fetchall()  # 输出查询结果
    return lines

def insert_UserInfo(username,password):
    sql = r"insert into UserInfo (username,password) values ('{}','{}')".format(username,password)
    cur.execute(sql)
    conn.commit()
    return 1
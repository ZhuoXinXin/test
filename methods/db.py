# coding:utf-8

import pymysql

conn = pymysql.connect(
    "localhost",
    "root",
    "root",
    "demo"
)
cur = conn.cursor()



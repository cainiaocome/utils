# -*- coding: utf-8 -*-

import string
import random
import pymysql

def random_string_gen(size=8):
    chars = string.ascii_letters + string.digits
    return ''.join(random.choice(chars) for _ in range(size))

def execute_sql(db='mail', sql=''):
    conn = pymysql.connect(host='localhost', port=3306, user='root', passwd='jialin,0204', db=db)
    cur = conn.cursor(pymysql.cursors.DictCursor)
    cur.execute(sql)
    res = cur.fetchall()
    return res

#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import MySQLdb

conn = MySQLdb.connect(host="189.0.1.82", port=3308, user="root", passwd="root", db="zcdb_maskjjx",charset="utf8")
cursor = conn.cursor()
cursor.execute('select * from tb_jddata')
values = cursor.fetchall()
print(values)

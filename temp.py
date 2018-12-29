from multiprocessing import Process
import cx_Oracle
conn =cx_Oracle.connect("kyle/kyle@168.0.1.25:1521/trans10g")
cursor = conn.cursor()
c = conn.cursor()
x = c.execute('select * from park_stock')
values = x.fetchone()
print(values)
c.close
conn.close


#测试用数据
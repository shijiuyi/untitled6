import psycopg2


conn = psycopg2.connect(database='flaskdb', user='postgres', password='123456',
                        host='localhost', port='5432')
print('connect success')

cur = conn.cursor()

"""
# 创建表
cur.execute('''CREATE TABLE COMPANY
       (ID INT PRIMARY KEY     NOT NULL,
       NAME           TEXT    NOT NULL,
       AGE            INT     NOT NULL,
       ADDRESS        CHAR(50),
       SALARY         REAL);''')
print('create table success')"""


"""
# 插入数据
cur.execute("insert into company(id, name, age, address, salary) "
            "values (1, 'zhangsan', 23, 'china henan', 12000)")
cur.execute("insert into company(id, name, age, address, salary) "
            "values (2, 'zfaf', 23, 'china henan', 14500)")
cur.execute("insert into company(id, name, age, address, salary) "
            "values (3, 'an', 23, 'china henan', 15900)")
print('insert success')"""

"""
# 查询数据
cur.execute("select id, name, address, salary from company")
rows = cur.fetchall()
for row in rows:
    print('id=', row[0])
    print('name=', row[1])
    print('address=', row[2])
    print('salary=', row[3]), "\n"
print("select success")"""

"""
# 更新数据
cur.execute("update company set salary = 15200 where id =1")
print("update success")"""

# 删除数据
cur.execute("delete from company where id =2;")
print("delete success")

conn.commit()
conn.close()

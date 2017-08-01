import sqlite3

# connecting to SQLite database

# if test.db didn't exist, it will create one
conn = sqlite3.connect('test.db')

# create oursor
cursor = conn.cursor()

# excute SQL command, create user table
cursor.execute('create table user (id varchar(20) primary key, name varchar (20))')

# excute SQL command, insert a record
cursor.execute('insert into user (id, name) values (\'1\',\'Michael\')')

# check row numbers
cursor.rowcount

# close cursor
cursor.close()

# commit
conn.commit()

# close connection
conn.close()



# query
conn = sqlite3.connect('test.db')
cursor = conn.cursor()
cursor.execute('select * from user where id=?', ('1',))
#通过featchall()可以拿到结果集。结果集是一个list，每个元素都是一个tuple，对应一行记录。
values = cursor.fetchall()
print(values)


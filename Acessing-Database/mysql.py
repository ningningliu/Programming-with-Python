import pymysql
#!/usr/bin/python3


# Open database connection
db = pymysql.connect("localhost","root","","Test" ) # host, username, password, database-name

# prepare a cursor object using cursor() method
cursor = db.cursor()

# execute SQL query using execute() method.
cursor.execute("select * from People")

# Fetch all row using fetchall() method.
data = cursor.fetchall()
for row in data :
    print (row[0], row[1])

# close the cursor object
cursor.close ()

# disconnect from server
db.close()

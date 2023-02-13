import mysql.connector

# establish the connection
conn = mysql.connector.connect(user='root', password='radara@121', host='localhost', database='mytest')

# create a cursor object
cursor = conn.cursor()

# execute the query to retrieve the server information
cursor.execute("SELECT @@version;")

# fetch the result
result = cursor.fetchone()

# print the result
print("Server Version:", result[0])

# close the cursor and the connection
cursor.close()
conn.close()

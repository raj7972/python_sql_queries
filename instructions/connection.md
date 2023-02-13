
To connect to a MySQL database from Python, we can use the mysql-connector-python library, which is an implementation of the MySQL Connector/Python, a pure Python driver for communicating with MySQL servers.

To Install MySQL connector module
```python 
pip install mysql-connector-python
```

In main.py file make the required imports 
```python
import mysql.connector
```
Use the connect() method of the MySQL Connector class with the required arguments to connect MySQL. It would return a MySQLConnection object if the connection established successfully.

Create Database in MySQL console
```shell
create database employee;
```

In main function create a cursor to interact with the database. we can check wheter we are connected or not by just ping the database above is theo code for checking the database connection
```python
def get_connection():
  try:
      cnx = mysql.connector.connect(user="<user_name>", password="<password>", host="<host_address>", database="<database_name>")

      if cnx.is_connected():
          cnx.ping(reconnect=True)
          print("MySQL server is up and running.")

  except mysql.connector.Error as e:
      print("Error:", e)

  finally:
    cnx.close()
    print("MySQL connection closed.")

if __name__=="__main__":
    database_conn(user=<user_name>,password=<password>,host=<host_name>,database=<database_name>)
```

Replace `<username>`, `<password>`, `<host_address>` and  `<database_name>` with your MySQL credentials.

NOTE: Providing credentials in source code is not a good practice. One should never do it, but save them in `.env` file and read from it. We are doing it here for simplicity.

Run the main.py file using the following command:

```shell
$ python3 run main.py
```

If everything it fine it will ping the database and print `MySQL server is up and running` in the terminal, else it will return the error. and it is always a good practice to close your database connection at the end.






Now, take a look at how to delete an entry from a database.

Create a delete function in main.py and pass the id as an argument

```python
import mysql.connector

    
def delete_employee_data(employee_id):
    cnx = mysql.connector.connect(user='root', password='radara@121',
                                  host='localhost', database='mytest')
    cursor = cnx.cursor()

    delete_query = "DELETE FROM employees WHERE id=%s"
    cursor.execute(delete_query, (employee_id,))

    cnx.commit()

    print(cursor.rowcount, "record(s) deleted.")

    cursor.close()
    cnx.close()
```

Explanation:

1. The mysql.connector module is imported to provide a Python driver for communicating with the database server.

2. A function named delete_employee_data is defined that takes one parameter: employee_id.

3. A connection to the database is established using the mysql.connector.connect method and a cursor object is created from the connection object.

4. The SQL DELETE statement is defined using the DELETE FROM employees WHERE id=%s format, where %s is a placeholder for the employee_id parameter.

5. The execute method of the cursor object is used to execute the DELETE statement, passing the employee_id parameter as an argument.

6. The cnx.commit method is called to persist the changes in the database.

7. The number of deleted records is printed using the rowcount property of the cursor object.

8. The cursor and connection objects are closed using the close method.

Call the delete_employee_data in dunder main 

```python
if __name__=="__main__":
    delete_employee_data(1)
```

you will see the below output in the command shell

```shell
1 record(s) deleted.
```
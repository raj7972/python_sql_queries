
Now, take a look at how to delete an entry from a database.

Create a delete function in main.py and pass the id as an argument

```python
import mysql.connector

    
def delete_employee_data(employee_id):

    delete_query = "DELETE FROM employees WHERE id=%s"
    cnx = get_connection()
    cursor = cnx.cursor()
    cursor.execute(delete_query, (employee_id,))

    cnx.commit()

    print(cursor.rowcount, "record(s) deleted.")

    cursor.close()
    cnx.close()
```

Explanation:

1. The mysql.connector module is imported to provide a Python driver for communicating with the database server.

2. A function named delete_employee_data is defined that takes one parameter: employee_id.

3. The SQL DELETE statement is defined using the DELETE FROM employees WHERE id=%s format, where %s is a placeholder for the employee_id parameter.

4. The execute method of the cursor object is used to execute the DELETE statement, passing the employee_id parameter as an argument.

5. The cnx.commit method is called to persist the changes in the database.

6. The number of deleted records is printed using the rowcount property of the cursor object.

7. The cursor and connection objects are closed using the close method.

Call the delete_employee_data in dunder main 

```python
if __name__=="__main__":
    delete_employee_data(1)
```

you will see the below output in the command shell

```shell
1 record(s) deleted.
```

## Excercise for SQL DELETE query using python

<THBREAK>

1. How would you delete all rows from a table named "employees" where the name is "John Doe" using Python and SQL?
    ```python
    A. conn.execute("DELETE FROM employees WHERE name='John Doe'")
    B. conn.execute("TRUNCATE TABLE employees WHERE name='John Doe'")
    C. conn.execute("DELETE * FROM employees WHERE name='John Doe'")
    ````

Answer: A

2. What is the correct syntax to delete a single row from a table named "employees" where the id is 1 using Python and SQL?
```python
    A. conn.execute("DELETE FROM employees WHERE id=1")     
    B. conn.execute("TRUNCATE TABLE employees WHERE id=1")
    C. conn.execute("DELETE * FROM employees WHERE id=1")
```

Answer: A

Note: In the above code snippets, it is assumed that the id column in the employees table is the primary key and the row with id=1 exists in the table.


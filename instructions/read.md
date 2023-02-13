
Now the employee details are inserted to the employee table no we can query the database and get the required employee details

In main.py write a new function `read_employee_data` function that will read the data from the database and print it.

Import the mysql connector to create a connection 

```python 
import mysql.connector

def read_employee_data():
    cnx = mysql.connector.connect(user='<username>', password='<password>',
                                  host='<host_address>', database='<database_name>')
    cursor = cnx.cursor()

    select_query = "SELECT * FROM employees"

    cursor.execute(select_query)
    employee_data = cursor.fetchall()
    return employee_data

    cursor.close()
    cnx.close()
```
## Step By Step Explanation for read_employee_data function

1. In the above read function the first step is to create a connection between MYSQL server and create a cursor to interact with the database.
Replace `<username>`, `<password>`, `<host_address>` and  `<database_name>` with your MySQL credentials. 

    ```python
    cnx = mysql.connector.connect(user=<username>, password=<password>,
                                host=<host>, database=<database>)
    cursor = cnx.cursor()
    ```
2. Execute the sql statement to get the employee details.
    ```python
       select_query = "SELECT * FROM employees"
    ```
3. We will use the fetchall() method to get all the entries from the database and close the database connection
    ```python
    employee_data = cursor.fetchall()
        return employee_data

        cursor.close()
        cnx.close()
    ```

# excerise related to SQl read query

<THBREAK>

1. What is the correct syntax to retrieve all rows from a table named "employees" using Python and SQL?

    ```python
    A. conn.execute("SELECT * FROM employees")
    B. conn.execute("SELECT name, position FROM employees")
    C. conn.execute("SELECT employees.* FROM employees")
    ```
<THBREAK>

Answer: A

<THBREAK>

2. How would you retrieve the name and salary columns from a table named "employees" and limit the results to only the first 2 rows using Python and SQL?

```python
    A. conn.execute("SELECT name, salary FROM employees LIMIT 2")
    B. conn.execute("SELECT * FROM employees LIMIT 2")
    C. conn.execute("SELECT name, salary FROM employees ORDER BY salary LIMIT 2")
```

<THBREAK>

Answer: A

<THBREAK>

3. What is the correct syntax to retrieve the name and position columns from a table named "employees" sorted by position in ascending order using Python and SQL?
```python
    A. conn.execute("SELECT name, position FROM employees ORDER BY position")
    B. conn.execute("SELECT name, position FROM employees ORDER BY position DESC")
    C. conn.execute("SELECT * FROM employees ORDER BY position")
```

<THBREAK>

Answer: A

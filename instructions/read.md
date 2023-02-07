
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
## Step By Step Explanation for getProduct function

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




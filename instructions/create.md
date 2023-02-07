
Now our database is connected to the database we will go ahead and start with the CRUD operations. we will create a table for `employee` in our database in which we store the `employee` related information The `employee` should have the following cable

| Column | Datatype | Description |
| --- | --- | --- |
| id | string | Unique identifier of the employer. |
| name | string | Name of the employee. |
| age | string | Age of the employee. |
| gender | string | Gender of the employee. |
| salary | string | salary of employee. |

## Create Method: Insert data to the database

As the employee table is newly created, it doesn't have any entries. so we start with the insert query.

```python
import mysql.connector

def insert_employee(name, age, gender, salary):
    cnx = mysql.connector.connect(user=<username>, password=<password>,
                                host=<host>, database=<database>)
    cursor = cnx.cursor()

    insert_query = "INSERT INTO employees (name, age, gender, salary) VALUES (%s, %s, %s, %s)"
    values = (name, age, gender, salary)

    cursor.execute(insert_query, values)
    cnx.commit()

    print("Data inserted successfully.")

    cursor.close()
    cnx.close()
```
## Step By Step Explanation for CreateProduct function

1. In the above insert function the first step is to create a connection between the MYSQL server and create a cursor to interact with the database.
Replace `<username>`, `<password>`, `<host_address>` and  `<database_name>` with your MySQL credentials. 

    ```python
    cnx = mysql.connector.connect(user=<username>, password=<password>,
                                host=<host>, database=<database>)
    cursor = cnx.cursor()
    ```
2. Execute the sql statement to insert the employee details.
    ```python
    insert_query = "INSERT INTO employees (name, age, gender, salary) VALUES (%s, %s, %s, %s)"
    values = (name, age, gender, salary)
    cursor.execute(insert_query, values)
    ```
3. Always commit the changes and close the database connection
    ```python
    cnx.commit()

    print("Data inserted successfully.")

    cursor.close()
    cnx.close()
    ```


    ```python
    if __name__=="__main__":
    insert("raj",21, Male, 10000)
    ```
You can add as many inserts and practice the SQL insert query



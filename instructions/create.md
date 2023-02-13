
Now our database is connected to the database we will go ahead and start with the CRUD operations. we will create a table for `employee` in our database in which we store the `employee` related information The `employee` should have the following cable

| Column | Datatype | Description |
| --- | --- | --- |
| id | int | Unique identifier of the employer. |
| name | string | Name of the employee. |
| age | int | Age of the employee. |
| position | string | position of the employee. |
| salary | Int | salary of employee. |

## Create Method: Insert data to the database

As the employee table is newly created, it doesn't have any entries. so we start with the insert query.

- Create a function get_connection to connect the database and Replace `<username>`, `<password>`, `<host_address>` and  `<database_name>` with your MySQL credentials and return the coonection.

```python
import mysql.connector

def get_connection():
    cnx = mysql.connector.connect(user="<username>", password="<password>",
                                host="<host_address>", database="<database>")
    return cnx

def insert_employee(name, age, position, salary):
   
    
    insert_query = "INSERT INTO employees (name, age, position, salary) VALUES (%s, %s, %s, %s)"
    values = (name, age, position, salary)
    cnx = get_connection()
    cursor = cnx.cursor()
    cursor.execute(insert_query, values)
    
    cnx.commit()

    print("Data inserted successfully.")

    cursor.close()
    cnx.close()
```
## Step By Step Explanation for insert_employee function

2. Write the the sql statement to insert the employee details.
    ```python
    insert_query = "INSERT INTO employees (name, age, position, salary) VALUES (%s, %s, %s, %s)"
    values = (name, age, position, salary)
    ```

2. Call the `get_connection` function, create a cursor to interact with database and execute the query
    ```python
    cnx = get_connection()
    cursor = cnx.cursor()
    cursor.execute(insert_query, values)
    ```

3. Always commit the changes and close the database connection and cursor with print statement
    ```python
    cnx.commit()

    print("Data inserted successfully.")

    cursor.close()
    cnx.close()
    ```


    ```python
    if __name__=="__main__":
    insert("john Doe",21, python, 10000)
    ```
You can add as many inserts and practice the SQL insert query

## excerice relate to python sql queries

<THBREAK>

1. What is the correct syntax to insert a single row into a table named "employees" using Python and SQL, while ignoring duplicates?
    ```python
    A. conn.execute("INSERT IGNORE INTO employees values ('John Doe', 25, 'Manager', 45000)")

    B. conn.execute("INSERT INTO employees (name, age, position, salary) values ('John Doe', 25, 'Manager', 45000) ON DUPLICATE KEY UPDATE")

    C. conn.execute("INSERT INTO employees (name, age, position, salary) values ('John Doe', 25, 'Manager', 45000) ON CONFLICT DO NOTHING")
    ```
Answer: A


2. How would you insert multiple rows into a table named "employees" using Python and SQL, and return the number of rows inserted?

    ```python
    A. conn.executemany("INSERT INTO employees values (?, ?, ?)", [('John Doe', 25, 'Manager', 45000), ('Jane Doe', 29 'Developer', 40000)])

    B. conn.executemany("INSERT INTO employees (name, age, position, salary) values (?, ?, ?)", [('John Doe', 25, 'Manager', 45000), ('Jane Doe', 29, 'Developer', 40000)])

    C. conn.executemany("INSERT INTO employees (name, age, position, salary) values (?, ?, ?)", [('John Doe', 25, 'Manager', 45000), ('Jane Doe', 29, 'Developer', 40000)], return_count=True)
    ```
Answer: B


3. How would you create a table "departments" with columns "id", "name", and "location" using Python and SQL?
```python
    A. conn.execute("CREATE TABLE departments (id INT, name TEXT, location TEXT)")
    B. conn.execute("CREATE TABLE departments (id INT PRIMARY KEY, name VARCHAR(50), location VARCHAR(50))")
    C. conn.execute("CREATE TABLE departments (id, name, location)")
```

Answer: B



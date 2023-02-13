
Now our database is connected to the database we will go ahead and start with the CRUD operations. we will create a table for `employee` in our database in which we store the `employee` related information The `employee` should have the following cable

| Column | Datatype | Description |
| --- | --- | --- |
| id | string | Unique identifier of the employer. |
| name | string | Name of the employee. |
| age | string | Age of the employee. |
| gender | string | Gender of the employee. |
| salary | Int | salary of employee. |

## Create Method: Insert data to the database

As the employee table is newly created, it doesn't have any entries. so we start with the insert query.

```python
import mysql.connector

def insert_employee(name, age, gender, position):
    cnx = mysql.connector.connect(user=<username>, password=<password>,
                                host=<host>, database=<database>)
    cursor = cnx.cursor()

    insert_query = "INSERT INTO employees (name, age, position, salary) VALUES (%s, %s, %s, %s)"
    values = (name, age, position, salary)

    cursor.execute(insert_query, values)
    cnx.commit()

    print("Data inserted successfully.")

    cursor.close()
    cnx.close()
```
## Step By Step Explanation for insert_employee function

1. In the above insert function the first step is to create a connection between the MYSQL server and create a cursor to interact with the database.
Replace `<username>`, `<password>`, `<host_address>` and  `<database_name>` with your MySQL credentials. 

    ```python
    cnx = mysql.connector.connect(user=<username>, password=<password>,
                                host=<host>, database=<database>)
    cursor = cnx.cursor()
    ```
2. Execute the sql statement to insert the employee details.
    ```python
    insert_query = "INSERT INTO employees (name, age, position, salary) VALUES (%s, %s, %s, %s)"
    values = (name, age, position, salary)
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
    insert("john Doe",21, python, 10000)
    ```
You can add as many inserts and practice the SQL insert query

## excerice relate to python sql queries

<THBREAK>

1. What is the correct syntax to insert a single row into a table named "employees" using Python and SQL, while ignoring duplicates?
    ```python
    A. conn.execute("INSERT IGNORE INTO employees values (1, 'John Doe', 'Manager')")

    B. conn.execute("INSERT INTO employees (id, name, position) values (1, 'John Doe', 'Manager') ON DUPLICATE KEY UPDATE")

    C. conn.execute("INSERT INTO employees (id, name, position) values (1, 'John Doe', 'Manager') ON CONFLICT DO NOTHING")
    ```
<THBREAK>
Answer: A

<THBREAK>

2. How would you insert multiple rows into a table named "employees" using Python and SQL, and return the number of rows inserted?

    ```python
    A. conn.executemany("INSERT INTO employees values (?, ?, ?)", [(1, 'John Doe', 'Manager'), (2, 'Jane Doe', 'Developer')])

    B. conn.executemany("INSERT INTO employees (id, name, position) values (?, ?, ?)", [(1, 'John Doe', 'Manager'), (2, 'Jane Doe', 'Developer')])

    C. conn.executemany("INSERT INTO employees (id, name, position) values (?, ?, ?)", [(1, 'John Doe', 'Manager'), (2, 'Jane Doe', 'Developer')], return_count=True)
    ```
<THBREAK>
Answer: B

<THBREAK>

3. How would you insert multiple rows into a table named "orders" using Python and SQL, and returning the generated primary key values for each row?

    ```python
    A. conn.executemany("INSERT INTO orders values (DEFAULT, ?, ?)", [('John Doe', '2022-01-01'), ('Jane Doe', '2022-01-02')])
    ```
    ```python
    B. conn.executemany("INSERT INTO orders (customer_name, order_date) values (?, ?)", [('John Doe', '2022-01-01'), ('Jane Doe', '2022-01-02')]
    )
    ```
    ```python
    C. cursor = conn.cursor() cursor.executemany("INSERT INTO orders     (customer_name, order_date) values (?, ?) RETURNING id", [('John Doe', '2022-01-01'), ('Jane Doe', '2022-01-02')]) 
    ids = [row[0] for row in cursor.fetchall()]
    print("Generated primary key values:", ids)
    ```

<THBREAK>
Answer: C



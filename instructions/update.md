
In the previous tasks, we created functions to insert the data into the database and read the data from the database. Now let's see how can we update the data which is already present in the database. Let's take a scenario in which the employee's salary is changed now we need to make the change in the database.

Create a update_details function in main.py and pass the employee_id and new_salary as an argument.

```python
def update_details(employee_id, new_salary):

    update_query = "UPDATE employees SET salary=%s WHERE id=%s"
    cnx = get_connection()
    cursor = cnx.cursor()

    cursor.execute(update_query, (new_salary, employee_id))

    cnx.commit()

    print(cursor.rowcount, "record(s) updated.")

    cursor.close()
    cnx.close()
```

Call the function in dunder main this is just for demonstartion.
```python
if __name__=="__main__:
    update_details(1,20000)
```

If the query is write will get "record(s) update" in shell.

## Excercise for update query

<THBREAK>

1. How would you update the salary of an employee with id 1 to the maximum salary of all employees using Python and SQL?
```python
    A. conn.execute("UPDATE employees SET salary=(SELECT MAX(salary) FROM employees) WHERE id=1")
    B. conn.execute("UPDATE employees SET salary=(SELECT salary FROM employees WHERE id=1)")
    C. conn.execute("UPDATE employees SET salary=MAX(salary) WHERE id=1")
```

Answer: A

2. How would you update the name of an employee with id 1 to the concatenation of their first name and last name using Python and SQL?
```python
    A. conn.execute("UPDATE employees SET name=first_name || ' ' || last_name WHERE id=1")
    B. conn.execute("UPDATE employees SET name=CONCAT(first_name, last_name) WHERE id=1")
    C. conn.execute("UPDATE employees SET name=first_name + last_name WHERE id=1")
```


Answer: A

Note: In the above code snippets, it is assumed that the columns `first_name`, `last_name`, `id`, and `name` exist in the employees `table`, and the table `departments` has `columns id`, name, and` department_id`.
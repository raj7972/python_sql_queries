
In the previous tasks, we created functions to insert the data into the database and read the data from the database. Now let's see how can we update the data which is already present in the database. Let's take a scenario in which the employee's salary is changed now we need to make the change in the database.

Create a update_details function in main.py and pass the employee_id and new_salary as an argument.

```python
def update_details(employee_id, new_salary):
    cnx = mysql.connector.connect(user='root', password='radara@121',
                                  host='localhost', database='mytest')
    cursor = cnx.cursor()

    update_query = "UPDATE employees SET salary=%s WHERE id=%s"
    cursor.execute(update_query, (new_salary, employee_id))

    cnx.commit()

    print(cursor.rowcount, "record(s) updated.")

    cursor.close()
    cnx.close()
```

Call the function in dunder main
```python
if __name__=="__main__:
    update_details(1,20000)
```

If the query is write will get "record(s) update" in shell.
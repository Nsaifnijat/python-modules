# -*- coding: utf-8 -*-
#its built in python 
import sqlite3
from sqlitFuncs import Employee
#create connection to the database sql, inside put the name of the database

#conn=sqlite3.connect('employee.db')
#the following creates a db in the Ram, everytime it starts the db fresh
conn=sqlite3.connect(':memory:')


#create cursor for sql commmands and table creation
c=conn.cursor()

#create table
c.execute('''
          CREATE TABLE employees(
              first text,
              last  text,
              pay   integer
              )
          
          ''')
          
#insert data into the table employee
c.execute("INSERT INTO employees VALUES('corey','5555',50000)")
#to actually let the data sit in the table
conn.commit()
#accessing the data
c.execute("SELECT * FROM employees WHERE last='5555' ")
c.fetchall()
#deletion command
c.execute('DELETE from employees WHERE last=:LAST',{"LAST":"5555"})

#to fetch data,

c.fetchone() #gets one sample
c.fetchmany(5) #gets exact number
c.fetchall() #gets all

c.fetchall()


emp1=Employee('john','Doe',7000)
emp2=Employee('jane','Doe',9000)
#three ways to insert the above data into the databse
#this method is open to sql injections
c.execute("INSERT INTO employees VALUES('{}','{}','{}')".format(emp1.first,emp1.last,emp1.pay))
#this method is more secure, ? means its string
c.execute("INSERT INTO employees VALUES(?,?,?)",(emp1.first,emp1.last,emp1.pay))
#this method is best practice
c.execute("INSERT INTO employees VALUES(:first,:last,:pay)",{'first':emp1.first,'last':emp1.last,'pay':emp1.pay})
#to access, method 1
c.execute("SELECT * FROM employees WHERE last=?", ('Doe',))
c.fetchall()
#to access, method 2 best practice

c.execute("SELECT * FROM employees WHERE last=:last", {'last':'Doe'})
c.fetchall()



#this part we use functions to insert update, or delete

def insert_emp(emp):
    #use the the with context manager to automatically commit the inserted data to the database
    with conn:
        c.execute("INSERT INTO employees VALUES(:first,:last,:pay)",{'first':emp.first,'last':emp.last,'pay':emp.pay})
def get_emps_by_name(lastname):
    c.execute("SELECT * FROM employees WHERE last=:last", {'last':'Doe'})
    return c.fetchall()
def update_pay(emp,pay):
    with conn:
        c.execute('''
                  UPDATE employees SET pay=:pay
                  WHERE first=:first AND last=:last''',
                  {'first':emp.first,'last':emp.last,'pay':pay})
def remove_emp(emp):
    with conn:
        c.execute('DELETE from employees WHERE first =:first AND last=:last',
                  {'first':emp.first,'last':emp.last})

emp1=Employee('john','Doe',7000)
emp2=Employee('jane','Doe',9000)

insert_emp(emp1)
insert_emp(emp2)

emps=get_emps_by_name('Doe')
print(emps)

update_pay(emp2, 800)

remove_emp(emp1)


conn.close()


c.execute('DELETE from userha where LoginID=84695992')

c.execute('DROP TABLE userha')



#inserting a list into sqlite
# Import the SQLite3 module
import sqlite3
db = sqlite3.connect(':memory:')
c = db.cursor()
c.execute('''CREATE TABLE users(id INTEGER PRIMARY KEY, name TEXT, phone TEXT)''')
users = [
    ('John', '5557241'), 
    ('Adam', '5547874'), 
    ('Jack', '5484522'), 
    ('Monthy',' 6656565')
]

c.executemany('''INSERT INTO users(name, phone) VALUES(?,?)''', users)
db.commit()

#selecting the column name
c.execute('''SELECT name FROM users''')

# Print the users
c.execute('''SELECT * FROM users''')
for row in c:
    print(row)

#return elements of a column a make it a list,
a=[]
# Print the users
c.execute('''SELECT name FROM users''')
for row in c:
    list(row)
    for i in row:
        a.append(i)
print(a)

db.close()



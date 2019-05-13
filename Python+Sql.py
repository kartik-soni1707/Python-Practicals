import mysql.connector
import os
mydb = mysql.connector.connect(
  host="localhost",
  user="username",
  passwd="password",
  database="table_name"
)
mc=mydb.cursor()
def prn():
    mc.execute("select * from table_name")
    print('###Table:###')
    for i in mc:
        print(i)
def add():
    wish='yes'
    while wish=='yes':
        name=input('Enter name:')
        age=input('Enter age:')
        mc.execute("INSERT INTO table_name VALUES('"+name+"',"+age+")""")
        mydb.commit()
        print('Addition cmpleted!!')
        wish=input('Do you wish to add more  ?')
def delete():    
    ans=input('Do you wish to delete ?')
    while ans=='yes':
        n1=input('Enter name to be deleted :')
        mc.execute("DELETE  FROM table_name WHERE name='"+n1+"'")
        mydb.commit()
        print('Deletion cmpleted!!')
        ans=input('Do you wish to delete more??')
print('     Welcome to MySql')
while 1:
    print('1>To Add New Data\n2>To Delete Old Data\n3>To View Data\n4>Exit')
    choice=int(input('Pls enter your choice:'))
    if choice==1:
        add()
    elif choice==2:
        delete()
    elif choice==3:
        prn()
    else:
        break
    
print('Thank you for using MySql :-)))')







import sqlite3
class DayCare():
 conn = sqlite3.connect('DayCare.db')
 print("open database successfully")




 conn.execute('''CREATE TABLE if not EXISTS DayCare(ID int primary key not null, name Text not null,  address char(50),
phone NUMBER  INTEGER, ownerName Text);''')

 conn.execute(''' CREATE TABLE if not EXISTS Parent (ID int primary key not null, ParentName CHAR(60), address char(50), phone NUMBER INTEGER); ''')

 conn.execute('''CREATE TABLE IF NOT EXISTS Child (ID int primary key not null, name Char(60), address CHAR(50), birthday INTEGER,
parentName CHAR(60));''')


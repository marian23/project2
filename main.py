import sqlite3
import sys
# select option
def display_main():
    print('1) search to day care\n'
          '2) Add child to record\n'
          '3) Add parent to record\n'
          '4) exit the program')
    # to search child or parent
def display_searchoption():
    print('1) serach by child name\n'
          '2) search by parent name\n'
            '3) exit the program')
# to create child table
def create_table_child():
    print(" print child table")
    conn = sqlite3.connect("DayCare.db")
    # it create child table in daycare
    conn.execute('''CREATE TABLE IF NOT EXISTS Child (
childName Char(60),
address CHAR(50),
birthday INTEGER,
parentName CHAR(60));''')

    conn.close()
    print("databse close")
# to create parent table
def create_table_parent():
    print("print parent table")
    conn = sqlite3.connect("DayCare.db")
    # it create parent table
    conn.execute(
        ''' CREATE TABLE if not EXISTS Parent (

  ParentName CHAR(60),
  address char(50),
  phoneNumber INTEGER, childName CHAR(60)); ''')

    conn.close()
    print("database close")
# to add child in child table
def add_child():
    print("add child data in the system")
    while True:
        try:
            childName = input("please enter the child name ")
            break
            # to check
        except ValueError:
            print("it is not valid enter")
    while True:
        try:
             address = input("prease enter the address where {} live ".format(childName))
             break

        except ValueError:
         print("it is not valid enter")

    while True:
        try:
                child_parent = input("Please enter the parentName of {}".format(childName))
                break
        except ValueError:
            print("it is not valid error")
    while True:
        try:
            child_birthday =  (input("please enter birthday of {} \n"
                           "if the birthday is march 2 2001 enter as 03022001 ".format(childName)))
            break
        except ValueError:
            print("it is not valid enter")

    conn = sqlite3.connect('DayCare.db')
    print('DB is open')
    print('add child method')
    # add to child information in the child table
    try:
        conn.execute('insert into child VALUES (?,?,?,?)', (childName, address,  child_birthday, child_parent, ))
        conn.commit()
    except Exception as e:
        print(e)
        print("your information may not save something got wrong")

    conn.close()

# add parent
def add_parent():
    print("add parent on the record")
    while True:
        try:
            parentName = input("please enter the parent name")
            break
        except ValueError:
            print(" sorry it is not valid enter")
    while True:
        try:
            address = input("please the addres where {} live".format(parentName))
            break
        except ValueError:
            print("sorry it is not valid enter")
    while True:
        try:
            phoneNumber = input("please enter the parent's phone number")
            break
        except ValueError:
            print("sorry it is not valid enter")
    while True:
        try:
            child_name = input("please enter parent's child name")
            break
        except ValueError:
            print("sorry it is not valid enter")

    conn = sqlite3.connect('DayCare.db')
    print('DB is open')
    print('add parent method')
    add_cursor2 = conn.cursor()
    try:
        # to add parent information in parent table
        add_cursor2.execute('INSERT INTO parent VALUES (?,?,?,?)', (parentName, address, phoneNumber, child_name))
   # except Exception:
        #print("your information may not save something got wrong")
        conn.commit()
        conn.close()
    except Exception:
        print("your information may not save something got wrong")
# to search child in system
def searchbychild():
    conn = sqlite3.connect('DayCare.db')
    print("open database successfuly")
    cursor = conn.cursor()
    cursor.execute("SELECT childName, address, birthday, parentName from Child")
    for row in cursor:
        print("childName =", row[0])
        print("address = ", row[1])
        print("birthday = ", row[2])
        print("parentName = ", row[3], "\n")
    conn.close()
# to search parent in system
def searchbyparent():
    conn = sqlite3.connect('DayCare.db')
    print("databas open successfull")
    cursor2 = conn.cursor()
    cursor2.execute("SELECT  parentName, address, phoneNumber, childName from Parent")
    for row in cursor2:
        print("parentName = ", row[0])
        print("address =", row[1])
        print("phoneNumber =", row[2])
        print("childName =", row[3], "\n")
    conn.close()



def main():
    # to call display_main
    print("welcome to child care")

    while True:
        display_main()
        main_choice = input(">>")

        #main_choice = input('please select option from the list')
        if main_choice == '1':
            while True:
                display_searchoption()
                search_bychoice = input("plrease select option from above")
                if search_bychoice == '1':
                    searchbychild()
                elif search_bychoice == '2':
                    searchbyparent()
                elif search_bychoice == '3':
                    print("exit program")

            print("accessing the search")
        elif main_choice == '2':
            add_child()
            print("accessing add the child")
        elif main_choice == '3':
            add_parent()
            print("accessing the add the parent")

        elif main_choice == '6':
            print("exit program")

            sys.exit()
create_table_child()
create_table_parent()

main()





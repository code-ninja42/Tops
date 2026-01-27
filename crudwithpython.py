import mysql.connector

try:
    mydb = mysql.connector.connect(
        host="localhost",
        user="root",
        password="",
        database="testing"
    )
    cursor = mydb.cursor()
    print("db connected")
except mysql.connector.Error as err:
    print("db not connected", err)
    exit()

def data_insert():
    try:
        id = int(input("Enter id: "))
        name = input("Enter name: ")
        adress = input("Enter address: ")
        city = input("Enter city: ")
        sql = "INSERT INTO Customer (id, name, adress, city) VALUES (%s, %s, %s, %s)"
        val = (id, name, adress, city)
        cursor.execute(sql, val)
        mydb.commit()
    except mysql.connector.Error as err:
        print("data not inserted", err)

def data_update():
    try:
        id = int(input("Enter id: "))
        name = input("Enter name: ")
        adress = input("Enter address: ")
        city = input("Enter city: ")
        sql = "UPDATE Customer SET name=%s, adress=%s, city=%s WHERE id=%s"
        val = (name, adress, city, id)
        cursor.execute(sql, val)
        mydb.commit()
    except mysql.connector.Error as err:
        print("data not updated", err)

def data_delete():
    try:
        id = int(input("Enter id: "))
        sql = "DELETE FROM Customer WHERE id=%s"
        val = (id,)
        cursor.execute(sql, val)
        mydb.commit()
    except mysql.connector.Error as err:
        print("data not deleted", err)

def data_fetch_all():
    try:
        cursor.execute("SELECT * FROM Customer")
        data = cursor.fetchall()
        for i in data:
            print(i)
    except mysql.connector.Error as err:
        print("data not fetched", err)

while True:
    print("1.Insert 2.Update 3.Delete 4.Fetch 5.Exit")
    ch = int(input("Enter choice: "))
    if ch == 1:
        data_insert()
    elif ch == 2:
        data_update()
    elif ch == 3:
        data_delete()
    elif ch == 4:
        data_fetch_all()
    elif ch == 5:
        break
    else:
        print("invalid choice")

cursor.close()
mydb.close()

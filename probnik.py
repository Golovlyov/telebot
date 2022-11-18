import pymysql


list_1 = {"bob", "cat"}
list_2 = set()

con = pymysql.connect('localhost', 'user17', 'password', 'mydb')

with con:
    cur = con.cursor()
    cur.execute("SELECT VERSION")
    version = cur.fetchone()

    print("Database version: {}". format(version[0]))


while open != "exit":
    open = str(input("vvedite name:   "))
    list_2.add(open)
    print(list_2)
    if open == "exit":
        break
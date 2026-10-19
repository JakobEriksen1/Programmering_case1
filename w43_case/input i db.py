import sqlite3
conn=sqlite3.connect("burgers.db")
cur=conn.cursor()


name = input("Skriv burgerns navn: ")
price = float(input("Skriv skriv burgerns pris: "))
calories = int(input("Skriv skriv burgerns kalorier: "))


cur.execute(
    "INSERT INTO burgers (NAME, PRICE, CALORIES) VALUES (?,?,?)",
    (name, price, calories)

)

conn.commit()

conn.close()

print("Burgeren er tilføjet til DB")
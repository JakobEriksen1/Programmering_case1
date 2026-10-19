import sqlite3
conn=sqlite3.connect("burgers.db")
cur=conn.cursor()

cur.execute("DELETE FROM BURGERS")

conn.commit()

print("Alle burgere er slettet fra databasen")


conn.close()
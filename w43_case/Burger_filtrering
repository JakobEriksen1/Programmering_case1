import sqlite3

conn = sqlite3.connect("burgers.db")
cur = conn.cursor()

# Vi får den til at vise burgere der højest koster 70kr.
cur.execute("SELECT NAME, PRICE, CALORIES FROM burgers WHERE PRICE <= 70 ORDER BY PRICE")

for name, price, calories in cur.fetchall():
    print(f"\nBurger: {name}")
    print(f"Pris: {price} kr.")
    print(f"Kalorier: {calories}")

conn.close()

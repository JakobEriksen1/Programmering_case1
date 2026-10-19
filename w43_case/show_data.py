import sqlite3
conn = sqlite3.connect('burgers.db')
cursor = conn.cursor()
for NAME,PRICE,CALORIES in cursor.execute("SELECT NAME,PRICE,CALORIES FROM burgers ORDER BY ID").fetchall():
       print(f"\nProduct name: {NAME}\nPrice: {int(PRICE)}Dkk\nCalories: {CALORIES}")


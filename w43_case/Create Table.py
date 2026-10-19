import sqlite3



conn = sqlite3.connect("burgers.db")
cur = conn.cursor()

cur.execute(
    """
    CREATE TABLE IF NOT EXISTS burgers (
        ID       INTEGER PRIMARY KEY AUTOINCREMENT,
        NAME     TEXT    NOT NULL UNIQUE,
        PRICE    REAL    NOT NULL,
        CALORIES INTEGER NOT NULL
    )
    """
)
conn.commit()
conn.close()
print("Tabellen 'burgers' er oprettet (eller fandtes allerede).")



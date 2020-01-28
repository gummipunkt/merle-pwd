import sqlite3
connection = sqlite3.connect("tresor_sql.db")

cursor = connection.cursor()

cursor.execute("SELECT * FROM entries")
print("fetchall:")
result = cursor.fetchall()
for r in result:
    print(r)
cursor.execute("SELECT * FROM entries")
print("\nfetch one:")
res = cursor.fetchone()
print(res)
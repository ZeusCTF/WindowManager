import sqlite3

conn = sqlite3.connect('customer.db')

c = conn.cursor()



c.execute("SELECT * FROM customers")
c.fetchall


input()

conn.commit()

conn.close
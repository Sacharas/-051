import sqlite3
conn = sqlite3.connect('orders.db')
cur = conn.cursor()
cur.execute("""CREATE TABLE IF NOT EXISTS users(
   userid INT PRIMARY KEY,
   fname TEXT,
   lname TEXT,
   gender TEXT);
""")
conn.commit()
cur.execute("""CREATE TABLE IF NOT EXISTS orders(
   orderid INT PRIMARY KEY,
   date TEXT,
   userid TEXT,
   total TEXT);
""")
conn.commit()
cur.execute("""INSERT INTO users(userid, fname, lname, gender) 
   VALUES('00001', 'Alex', 'Smith', 'male');""")
conn.commit()
more_users = [('00003', 'Peter', 'Parker', 'Male'), ('00004', 'Bruce', 'Wayne', 'male')]
cur.executemany("INSERT INTO users VALUES(?, ?, ?, ?);", more_users)
conn.commit()

cur.executemany("INSERT INTO users VALUES(?, ?, ?, ?);", customers)
cur.executemany("INSERT INTO orders VALUES(?, ?, ?, ?);", orders)
conn.commit()
cur.execute("SELECT * FROM users;")
one_result = cur.fetchone()
print(one_result)

import sqlite3

conn = sqlite3.connect("craftyrafty.db")

conn.execute("""
CREATE TABLE IF NOT EXISTS users (
    id INTEGER PRIMARY KEY,
    username TEXT,
    password TEXT
)
""")

conn.execute("""
CREATE TABLE IF NOT EXISTS products (
    id INTEGER PRIMARY KEY,
    name TEXT,
    price REAL,
    description TEXT
)
""")

conn.execute("INSERT INTO users VALUES (1, 'admin', 'admin123')")
conn.execute("INSERT INTO users VALUES (2, 'artist1', 'password')")
conn.execute("INSERT INTO products VALUES (1, 'Handmade Vase', 29.99, 'Ceramic vase')")
conn.execute("INSERT INTO products VALUES (2, 'Woven Basket', 45.00, 'Hand-woven basket')")
conn.execute("INSERT INTO products VALUES (3, 'Oil Painting', 120.00, 'Original artwork')")

conn.commit()
conn.close()
print("CraftyRafty database created.")
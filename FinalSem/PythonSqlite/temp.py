import sqlite3
conn = sqlite3.connect('test.db')
cursor = conn.cursor()
# Create table
cursor.execute('''CREATE TABLE IF NOT EXISTS users (id INTEGER PRIMARY KEY, name TEXT, email TEXT)''')
# Insert data
cursor.execute("INSERT INTO users (name, email) VALUES ('Alice', 'alice@test.com')")
# Show data
conn.commit()
cursor.execute("SELECT * FROM users")
print(cursor.fetchall())
conn.close()

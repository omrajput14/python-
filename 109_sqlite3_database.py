# SQLite3 Database Example
import sqlite3

def setup_db():
    conn = sqlite3.connect(':memory:') # In-memory database
    c = conn.cursor()
    c.execute('''CREATE TABLE users (id INTEGER PRIMARY KEY, name TEXT, age INTEGER)''')
    
    users = [(1, 'Alice', 30), (2, 'Bob', 25)]
    c.executemany('INSERT INTO users VALUES (?,?,?)', users)
    conn.commit()
    
    print("Users in database:")
    for row in c.execute('SELECT * FROM users'):
        print(row)
    conn.close()

if __name__ == "__main__":
    setup_db()

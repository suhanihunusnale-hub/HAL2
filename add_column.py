import sqlite3

conn = sqlite3.connect("database.db")

cursor = conn.cursor()

try:

    cursor.execute("""
    ALTER TABLE messages
    ADD COLUMN decrypt_attempts INTEGER DEFAULT 0
    """)

    print("decrypt_attempts column added successfully")

except sqlite3.OperationalError:

    print("Column already exists")


conn.commit()

conn.close()
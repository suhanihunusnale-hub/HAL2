import sqlite3

conn = sqlite3.connect("database.db")
cursor = conn.cursor()

cursor.execute("""
ALTER TABLE messages
ADD COLUMN decrypt_attempts INTEGER DEFAULT 0
""")

conn.commit()
conn.close()

print("decrypt_attempts column added successfully.")
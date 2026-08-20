import sqlite3

conn = sqlite3.connect("database.db")
cursor = conn.cursor()

# Get all table names
cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
tables = cursor.fetchall()

for table in tables:
    table_name = table[0]
    print(f"\n===== {table_name.upper()} =====")

    cursor.execute(f"SELECT * FROM {table_name}")
    rows = cursor.fetchall()

    if rows:
        for row in rows:
            print(row)
    else:
        print("No data found.")

conn.close()
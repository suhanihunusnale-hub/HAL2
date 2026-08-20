import sqlite3
from datetime import datetime


DATABASE="database.db"



def add_log(username, action):

    conn = sqlite3.connect(
        DATABASE
    )

    cursor = conn.cursor()


    cursor.execute(
    """
    INSERT INTO audit_logs
    (username,action,log_time)
    VALUES(?,?,?)
    """,
    (
        username,
        action,
        datetime.now()
    )
    )


    conn.commit()

    conn.close()
from flask import Flask, render_template, request, redirect, session
import sqlite3
from datetime import datetime

from bb84 import generate_quantum_key, detect_eavesdropping
from encryption import encrypt_message, decrypt_message
from threat_detection import check_threat
from audit import add_log


app = Flask(__name__)

app.secret_key = "Quantum_Defence_Secret_Key"

DATABASE = "database.db"



# ---------------- DATABASE CONNECTION ----------------

def get_db():

    conn = sqlite3.connect(DATABASE)

    conn.row_factory = sqlite3.Row

    return conn



# ---------------- CREATE DATABASE ----------------

def create_database():

    conn = sqlite3.connect(DATABASE)

    cursor = conn.cursor()


    cursor.execute("""
    CREATE TABLE IF NOT EXISTS users(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        username TEXT UNIQUE,
        password TEXT,
        role TEXT
    )
    """)


    cursor.execute("""
    CREATE TABLE IF NOT EXISTS messages(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        sender TEXT,
        receiver TEXT,
        original_message TEXT,
        encrypted_message TEXT,
        quantum_key TEXT,
        timestamp TEXT,
        status TEXT
    )
    """)


    cursor.execute("""
    CREATE TABLE IF NOT EXISTS threats(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        threat_type TEXT,
        severity TEXT,
        description TEXT,
        detected_time TEXT
    )
    """)


    cursor.execute("""
    CREATE TABLE IF NOT EXISTS audit_logs(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        username TEXT,
        action TEXT,
        log_time TEXT
    )
    """)



    users=[

        ("admin","admin123","Administrator"),

        ("commander01","cmd123","Commander"),

        ("officer01","off123","Field Officer"),

        ("analyst01","ana123","Security Analyst")

    ]


    for user in users:

        try:

            cursor.execute(
            """
            INSERT INTO users
            (username,password,role)

            VALUES(?,?,?)
            """,
            user
            )

        except:

            pass



    conn.commit()

    conn.close()





# ---------------- LOGIN ----------------


@app.route("/", methods=["GET","POST"])

def login():


    if request.method=="POST":


        username=request.form["username"]

        password=request.form["password"]

        role=request.form["role"]



        conn=get_db()


        user=conn.execute(

        """
        SELECT * FROM users

        WHERE username=?
        AND password=?
        AND role=?

        """,

        (
        username,
        password,
        role
        )

        ).fetchone()



        conn.close()



        if user:


            session["username"]=username

            session["role"]=role


            add_log(
                username,
                "Logged into system"
            )


            return redirect(
                "/dashboard"
            )


    return render_template(
        "login.html"
    )





# ---------------- DASHBOARD ----------------


@app.route("/dashboard")

def dashboard():


    if "username" not in session:

        return redirect("/")



    return render_template(

        "dashboard.html",

        username=session["username"],

        role=session["role"]

    )





# ---------------- SEND MESSAGE ----------------
@app.route("/sender", methods=["GET", "POST"])
def sender():

    if "username" not in session:
        return redirect("/")

    conn = get_db()
    cursor = conn.cursor()

    # Get all users except the logged-in user
    cursor.execute("""
        SELECT username, role
        FROM users
        WHERE username != ?
    """, (session["username"],))

    receivers = cursor.fetchall()

    success = None

    if request.method == "POST":

        sender = session["username"]
        receiver = request.form["receiver"]
        message = request.form["message"]

        quantum_key = generate_quantum_key()

        encrypted_message = encrypt_message(
            message,
            quantum_key
        )

        cursor.execute("""
        INSERT INTO messages
        (
            sender,
            receiver,
            original_message,
            encrypted_message,
            quantum_key,
            timestamp,
            status,
            decrypt_attempts
        )
        VALUES (?, ?, ?, ?, ?, datetime('now'), ?, ?)
        """,
        (
            sender,
            receiver,
            message,
            encrypted_message,
            quantum_key,
            "Encrypted",
            0
        ))

        conn.commit()

        print("Sender :", sender)
        print("Receiver :", receiver)
        print("Message :", message)

        add_log(
            session["username"],
            "Sent encrypted message"
        )

        success = "✅ Secure Message Sent Successfully"

    conn.close()

    return render_template(
        "sender.html",
        receivers=receivers,
        success=success
    )
@app.route("/receiver", methods=["GET", "POST"])
def receiver():

    if "username" not in session:
        return redirect("/")

    receiver_name = session["username"]

    conn = get_db()
    cursor = conn.cursor()

    decrypted_message = ""

    # ---------------- DECRYPT ----------------
    if request.method == "POST":

        message_id = request.form["id"]

        cursor.execute("""
        SELECT
            encrypted_message,
            quantum_key,
            decrypt_attempts
        FROM messages
        WHERE id=?
        """, (message_id,))

        row = cursor.fetchone()

        if row:

            encrypted = row["encrypted_message"]
            quantum_key = row["quantum_key"]
            attempts = row["decrypt_attempts"]

            if attempts >= 3:

                decrypted_message = "🔒 Maximum decryption attempts reached."

            else:

                decrypted_message = decrypt_message(
                    encrypted,
                    quantum_key
                )

                attempts += 1

                cursor.execute("""
                UPDATE messages
                SET
                    status=?,
                    decrypt_attempts=?
                WHERE id=?
                """,
                (
                    "Delivered",
                    attempts,
                    message_id
                ))

                conn.commit()

    # ---------------- INBOX ----------------
    cursor.execute("""
    SELECT
        id,
        sender,
        receiver,
        original_message,
        encrypted_message,
        quantum_key,
        timestamp,
        status,
        decrypt_attempts
    FROM messages
    WHERE receiver=?
    ORDER BY id DESC
    """, (receiver_name,))

    messages = cursor.fetchall()

    conn.close()

    return render_template(
        "receiver.html",
        receiver=receiver_name,
        messages=messages,
        decrypted_message=decrypted_message
    )
    print("Messages:")
    for msg in messages:
        print(dict(msg))
# ---------------- DECRYPT MESSAGE ----------------

@app.route("/decrypt/<int:id>")
def decrypt(id):


    if "username" not in session:

        return redirect("/")


    conn=get_db()


    msg=conn.execute(

    """
    SELECT * FROM messages
    WHERE id=?
    """,

    (id,)

    ).fetchone()



    conn.close()

    if msg is None:
        return "Message not found", 404

    decrypted=decrypt_message(

        msg["encrypted_message"],

        msg["quantum_key"]

    )

    decrypted=decrypt_message(

        msg["encrypted_message"],

        msg["quantum_key"]

    )



    add_log(

        session["username"],

        "Decrypted secure message"

    )


    return render_template(

        "decrypt.html",

        message=decrypted,

        sender=msg["sender"],

        time=msg["timestamp"]

    )

# ---------------- THREAT MONITOR ----------------


@app.route("/threats")

def threats():


    result=check_threat()



    if result:


        conn=get_db()


        conn.execute(

        """

        INSERT INTO threats

        (
        threat_type,
        severity,
        description,
        detected_time
        )

        VALUES(?,?,?,?)

        """,

        (

        result[0],

        result[1],

        result[2],

        datetime.now()

        )

        )


        conn.commit()

        conn.close()



    conn=get_db()


    data=conn.execute(

    """

    SELECT * FROM threats

    """

    ).fetchall()



    conn.close()



    return render_template(

        "threats.html",

        threats=data

    )





# ---------------- AUDIT LOGS ----------------


@app.route("/logs")

def logs():


    conn=get_db()


    logs=conn.execute(

    """

    SELECT * FROM audit_logs

    ORDER BY id DESC

    """

    ).fetchall()



    conn.close()



    return render_template(

        "logs.html",

        logs=logs

    )





# ---------------- LOGOUT ----------------


@app.route("/logout")

def logout():

    session.clear()

    return redirect("/")





if __name__=="__main__":

    create_database()

    app.run(debug=True)
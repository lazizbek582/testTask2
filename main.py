import sqlite3

DATABASE_FILE = "users.db"


def create_table():
    with sqlite3.connect(DATABASE_FILE) as conn:
        cursor = conn.cursor()
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS users (
                id INTEGER PRIMARY KEY,
                name TEXT NOT NULL,
                age INTEGER NOT NULL,
                email TEXT NOT NULL
            )
        ''')
        conn.commit()


def add_user(name, age, email):
    with sqlite3.connect(DATABASE_FILE) as conn:
        cursor = conn.cursor()
        cursor.execute("INSERT INTO users (name, age, email) VALUES (?, ?, ?)", (name, age, email))
        conn.commit()


def get_user(user_id):
    with sqlite3.connect(DATABASE_FILE) as conn:
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM users WHERE id=?", (user_id,))
        return cursor.fetchone()


def update_user(user_id, name, age, email):
    with sqlite3.connect(DATABASE_FILE) as conn:
        cursor = conn.cursor()
        cursor.execute("UPDATE users SET name=?, age=?, email=? WHERE id=?", (name, age, email, user_id))
        conn.commit()


def delete_user(user_id):
    with sqlite3.connect(DATABASE_FILE) as conn:
        cursor = conn.cursor()
        cursor.execute("DELETE FROM users WHERE id=?", (user_id,))
        conn.commit()


if __name__ == "__main__":

    add_user("Laziz Qaxorov", 27, "lazizbek583@gmail.com")
    add_user("Aziz Qaxorov", 26, "aziz583@gmail.com")

    user_id = 2
    user = get_user(user_id)
    if user:
        print(f"User with ID {user_id}: {user[1]}, {user[2]} years old, email: {user[3]}")
    else:
        print(f"User with ID {user_id} not found.")

    update_user(user_id, "Aziz Qaxorov", 26, "aziz583@gmail.com")

    user = get_user(user_id)
    if user:
        print(f"Updated user with ID {user_id}: {user[1]}, {user[2]} years old, email: {user[3]}")

    delete_user(user_id)
    user = get_user(user_id)
    if user:
        print(f"User with ID {user_id} still exists.")
    else:
        print(f"User with ID {user_id} has been deleted.")

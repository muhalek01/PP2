import csv
from pathlib import Path

from connect import BASE_DIR, get_connection, run_sql_file


def ask(prompt, default=None):
    """Read a console value and allow Enter to accept a default."""
    value = input(f"{prompt}{f' [{default}]' if default is not None else ''}: ").strip()
    return value or default


def setup_database():
    """Create the Practice 7 table and stored procedures."""
    run_sql_file("schema.sql")
    run_sql_file("procedures.sql")
    print("Database is ready.")


def add_contact(username, phone):
    """Insert a new contact or update phone when the username already exists."""
    with get_connection() as conn, conn.cursor() as cur:
        cur.execute("CALL upsert_contact(%s, %s)", (username, phone))


def add_contact_interactive():
    """Add one contact from console input."""
    add_contact(ask("Username"), ask("Phone"))
    print("Contact saved.")


def import_csv(path):
    """Import contacts from a CSV file with username/name and phone columns."""
    with Path(path).open(encoding="utf-8", newline="") as file:
        for row in csv.DictReader(file):
            username = (row.get("username") or row.get("name") or "").strip()
            phone = (row.get("phone") or "").strip()
            if username and phone:
                add_contact(username, phone)
    print("CSV import finished.")


def print_rows(rows):
    if not rows:
        print("No contacts found.")
        return
    for row in rows:
        print(f"{row['id']}: {row['username']} - {row['phone']} ({row['created_at']})")


def search_contacts():
    """Search by username substring and/or phone prefix."""
    username = ask("Username contains", "")
    phone_prefix = ask("Phone prefix", "")
    with get_connection(dict_rows=True) as conn, conn.cursor() as cur:
        cur.execute("SELECT * FROM search_contacts(%s, %s)", (username, phone_prefix))
        print_rows(cur.fetchall())


def update_contact():
    """Update only the fields required by the task: username or phone."""
    field = ask("Update field (username / phone)", "phone")
    with get_connection() as conn, conn.cursor() as cur:
        if field == "username":
            cur.execute("CALL update_contact_name(%s, %s)", (ask("Old username"), ask("New username")))
        elif field == "phone":
            cur.execute("CALL update_contact_phone(%s, %s)", (ask("Username"), ask("New phone")))
        else:
            print("Unknown field.")
            return
    print("Updated.")


def delete_contact():
    """Delete by username or by exact phone number."""
    with get_connection() as conn, conn.cursor() as cur:
        cur.execute("CALL delete_contact(%s)", (ask("Username or phone")))
    print("Deleted if a matching contact existed.")


def menu():
    actions = {
        "1": ("Setup database", setup_database),
        "2": ("Add contact", add_contact_interactive),
        "3": ("Import CSV", lambda: import_csv(ask("CSV path", str(BASE_DIR / "contacts.csv")))),
        "4": ("Search contacts", search_contacts),
        "5": ("Update contact", update_contact),
        "6": ("Delete contact", delete_contact),
    }

    while True:
        print("\nPractice 7 PhoneBook")
        for key, (title, _action) in actions.items():
            print(f"{key}. {title}")
        print("0. Quit")

        choice = input("> ").strip()
        if choice == "0":
            break
        if choice in actions:
            actions[choice][1]()
        else:
            print("Unknown choice.")


if __name__ == "__main__":
    menu()

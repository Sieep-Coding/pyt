import sqlite3

def init_database():
    conn = sqlite3.connect("business_contacts.db")
    cursor = conn.cursor()

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS contacts (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        business_name TEXT,
        contact_name TEXT,
        email TEXT,
        phone TEXT,
        status TEXT
    )
    """)
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS projects (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        project_name TEXT,
        proj_contact_name TEXT,
        proj_email TEXT,
        proj_phone TEXT,
        proj_status TEXT
    )
    """)

    cursor.execute("SELECT COUNT(*) FROM contacts")
    cursor.execute("SELECT COUNT(*) FROM projects")
    # if cursor.fetchone()[0] == 0:
    #     for business in BUSINESS_NAMES:
    #         contact_name = f"Contact {randint(1, 100)}"
    #         email = f"{contact_name.lower().replace(' ', '_')}@example.com"
    #         phone = f"{randint(100, 999)}-{randint(100, 999)}-{randint(1000, 9999)}"
    #         status = choice(["Lead", "Active", "Inactive"])
    #         cursor.execute(
    #             "INSERT INTO contacts (business_name, contact_name, email, phone, status) VALUES (?, ?, ?, ?, ?)",
    #             (business, contact_name, email, phone, status)
    #         )
    conn.commit()
    conn.close()

def fetch_contacts():
    conn = sqlite3.connect("business_contacts.db")
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM contacts")
    contacts = cursor.fetchall()
    conn.close()
    return contacts

def add_contact(business_name, contact_name, email, phone, status):
    conn = sqlite3.connect("business_contacts.db")
    cursor = conn.cursor()
    cursor.execute(
        "INSERT INTO contacts (business_name, contact_name, email, phone, status) VALUES (?, ?, ?, ?, ?)",
        (business_name, contact_name, email, phone, status)
    )
    conn.commit()
    conn.close()

def update_contact(business_name, contact_name, email, phone, status):
    conn = sqlite3.connect("business_contacts.db")
    cursor = conn.cursor()
    cursor.execute(
        "UPDATE contacts (business_name, contact_name, email, phone, status) VALUES (?, ?, ?, ?, ?)",
        (business_name, contact_name, email, phone, status)
    )
    conn.commit()
    conn.close()

def fetch_projects():
    conn = sqlite3.connect("business_contacts.db")
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM projects")
    projects = cursor.fetchall()
    conn.close()
    return projects

def add_project(project_name, proj_contact_name, proj_email, proj_phone, proj_status):
    conn = sqlite3.connect("business_contacts.db")
    cursor = conn.cursor()
    cursor.execute(
        "INSERT INTO projects (project_name, proj_contact_name, proj_email, proj_phone, proj_status) VALUES (?, ?, ?, ?, ?)",
        (project_name, proj_contact_name, proj_email, proj_phone, proj_status)
    )
    conn.commit()
    conn.close()

def delete_project(project_id):
    conn = sqlite3.connect("business_contacts.db")
    cursor = conn.cursor()
    cursor.execute("DELETE FROM projects WHERE id = ?", (project_id,))
    conn.commit()
    conn.close()

def delete_contact(contact_id):
    conn = sqlite3.connect("business_contacts.db")
    cursor = conn.cursor()
    cursor.execute("DELETE FROM contacts WHERE id = ?", (contact_id,))
    conn.commit()
    conn.close()

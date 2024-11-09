import sqlite3
from datetime import datetime

# Register datetime adapter and converter
def adapt_datetime(value):
    return value.isoformat()  # Convert datetime to ISO 8601 string format

def convert_datetime(value):
    return datetime.fromisoformat(value)  # Convert string back to datetime object

sqlite3.register_adapter(datetime, adapt_datetime)
sqlite3.register_converter("datetime", convert_datetime)

def initialize_database():
    conn = sqlite3.connect('contacts.db', detect_types=sqlite3.PARSE_DECLTYPES)  # Enable datetime parsing
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS contacts (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            number TEXT NOT NULL,
            email TEXT NOT NULL,
            created_at TIMESTAMP,
            notes TEXT
        )
    ''')
    conn.commit()
    conn.close()

def add_contact():
    name = input("Please enter your name: ")
    number = input("Please enter your number: ")
    email = input("Please enter your email: ")
    notes = input("Any additional notes (optional): ")
    
    conn = sqlite3.connect('contacts.db', detect_types=sqlite3.PARSE_DECLTYPES)  # Enable datetime parsing
    cursor = conn.cursor()
    cursor.execute('''
        INSERT INTO contacts (name, number, email, created_at, notes)
        VALUES (?, ?, ?, ?, ?)
    ''', (name, number, email, datetime.now(), notes))  # Store current datetime
    conn.commit()
    conn.close()
    print("Contact added successfully!")

def show_contact():
    conn = sqlite3.connect('contacts.db', detect_types=sqlite3.PARSE_DECLTYPES)  # Enable datetime parsing
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM contacts')
    contacts = cursor.fetchall()
    
    if not contacts:
        print("No contacts available.")
        return
        
    print("\n-------- Contacts --------")
    for contact in contacts:
        print(f"\nID: {contact[0]}")
        print(f"Name: {contact[1]}")
        print(f"Number: {contact[2]}")
        print(f"Email: {contact[3]}")
        print(f"Created: {contact[4]}")  # This should now be a datetime object
        if contact[5]:  # If notes exist
            print(f"Notes: {contact[5]}")
        print("-" * 25)
    conn.close()

def remove_contact():
    show_contact()  # Show contacts first
    contact_id = input("\nEnter the ID of the contact to remove: ")
    
    conn = sqlite3.connect('contacts.db', detect_types=sqlite3.PARSE_DECLTYPES)  # Enable datetime parsing
    cursor = conn.cursor()
    cursor.execute('DELETE FROM contacts WHERE id = ?', (contact_id,))
    if cursor.rowcount > 0:
        print("Contact removed successfully!")
    else:
        print("Contact not found.")
    conn.commit()
    conn.close()

def search_contacts():
    search_term = input("Enter name or number to search: ")
    conn = sqlite3.connect('contacts.db', detect_types=sqlite3.PARSE_DECLTYPES)  # Enable datetime parsing
    cursor = conn.cursor()
    cursor.execute('''
        SELECT * FROM contacts 
        WHERE name LIKE ? OR number LIKE ? OR email LIKE ?
    ''', (f'%{search_term}%', f'%{search_term}%', f'%{search_term}%'))
    results = cursor.fetchall()
    
    if results:
        print("\n-------- Search Results --------")
        for contact in results:
            print(f"\nID: {contact[0]}")
            print(f"Name: {contact[1]}")
            print(f"Number: {contact[2]}")
            print(f"Email: {contact[3]}")
    else:
        print("No matching contacts found.")
    conn.close()

# Initialize database and start main program
initialize_database()

while True:
    print("\n1. Add Contact")
    print("2. Remove Contact")
    print("3. Show All Contacts")
    print("4. Search Contacts")
    print("5. Exit")
    
    choice = input("\nEnter your choice (1-5): ")
    
    if choice == '1':
        add_contact()
    elif choice == '2':
        remove_contact()
    elif choice == '3':
        show_contact()
    elif choice == '4':
        search_contacts()
    elif choice == '5':
        print("Program stopped.")
        break
    else:
        print("Invalid choice, please try again.")

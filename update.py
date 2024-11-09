import json # import json module
# Import json module to handle reading and writing JSON files
# This allows us to store contacts persistently between program runs

#` Untracked` files are files that are not being tracked by git

 
# Cursor is a code editor that allows us to write code and see the output in real-time 
# what is chemistry?
# chemistry is the study of matter and its properties, and the changes it undergoes.    
# what is physics?  
# physics is the study of matter and energy and their interactions.
# Do you know Elon Musk?
# Elon Musk is a South African-born Canadian-American entrepreneur and businessman who co-founded PayPal and founded SpaceX, Neuralink, and The Boring Company.
# Do you know Gabaxey?
# Gabaxey is a software engineer and a founder of a software company called "The Boring Company"

store = []

def save_contacts():
    with open("contacts.json", "w") as file: # write to the file
        json.dump(store, file)

def load_contacts():
    global store
    try:
        with open("contacts.json", "r") as file: # read the file
            store = json.load(file)
    except FileNotFoundError:
        store = []

def add_contact():
    store.append([
        input("Please enter your name: "),
        input("Please enter your number: "),
        input("Please enter your email: ")
    ])

def remove_contact():
    name = input("Enter the name of the contact to remove: ")
    for contact in store:
        if contact[0] == name:
            store.remove(contact)
            print("Contact removed successfully.")
            return
    print("Contact not found.")

def show_contact():
    if not store:
        print("No contacts available.")
        return
    print("-------- Contacts --------")
    for contact in store:
        print(f"Name: {contact[0]}, Number: {contact[1]}, Email: {contact[2]}")
    print("--------------------------")

# Load contacts when the program starts
load_contacts()

# Main Program Loop
while True:
    print("\n1. Add Contact\n2. Remove Contact\n3. Show Contacts\n4. Exit")
    choice = input("Enter your choice (1-4): ")
    
    if choice == '1':
        add_contact()
    elif choice == '2':
        remove_contact()
    elif choice == '3':
        show_contact()
    elif choice == '4':
        save_contacts()  # Save contacts before exiting
        print("Program stopped.")
        break
    else:
        print("Invalid choice, please try again.")

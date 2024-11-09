
# TODO: Fix indentation errors

store = []

def add_contact():
    name = input("Please enter your name: ")
    number = input("Please enter your number: ")
    email = input("Please enter your email: ")

    # Add contact details to the store
    contact_list = [name, number, email]
    store.append(contact_list)  # Only append to store here

def remove_contact():
    contact_to_remove = input("Enter the name of the contact to remove: ")
    for contact in store:
        if contact[0] == contact_to_remove:
            store.remove(contact)  # Fix indentation here
            print("Contact removed successfully.")
            return  # Stop the loop after removal
    print("Contact not found.")

def show_contact():
    if not store:
        print("No contacts available.")
    else:
        print("---------- Contacts ----------")
        for contact in store:
            print("Name:", contact[0])
            print("Number:", contact[1])
            print("Email:", contact[2])
            print("------------------------------")

# Main Program Loop
my_running = True
while my_running:
    print("\n1. Add Contact")
    print("2. Remove Contact")
    print("3. Show Contact")
    print("4. Exit")
    
    choice = input("Enter your choice (1-4): ")

    if choice == '1':
        add_contact()
    elif choice == '2':
        remove_contact()
    elif choice == '3':
        show_contact()
    elif choice == '4':
        my_running = False
    else:
        print("Invalid choice, please try again.")

print("Program stopped.")
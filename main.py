store = []

def add_contact():
    store.append([input("Name: "), input("Number: "), input("Email: ")])

def remove_contact():
    name = input("Name to remove: ")
    for contact in store:
        if contact[0] == name:
            store.remove(contact)
            print("Contact removed.")
            return
    print("Not found.")

def show_contact():
    if not store:
        print("No contacts.")
        return
    for contact in store:
        print(f"\nName: {contact[0]}\nNumber: {contact[1]}\nEmail: {contact[2]}\n---")

while True:
    choice = input("\n1:Add 2:Remove 3:Show 4:Exit\nChoice: ")
    if choice == '1': add_contact()
    elif choice == '2': remove_contact() 
    elif choice == '3': show_contact()
    elif choice == '4': break
    else: print("Invalid choice.")

print("Program stopped.")



# 📞 Contact Management System

A simple command-line contact management system built in Python that allows users to store, manage, and persist contact information using JSON file storage. 

## ✨ Features

- ➕ Add new contacts with name, phone number, and email
- ❌ Remove existing contacts by name  
- 📋 Display all stored contacts
- 💾 Persistent data storage using JSON
- 🔄 Auto-load contacts on startup
- 💫 Auto-save contacts on exit

## 🛠️ How It Works

The program uses a JSON-based storage system to maintain contact information between sessions. The main data structure (`store`) is a list that holds contact information as nested lists.

### 🔑 Core Functions

1. **📥 Contact Storage**
   - `save_contacts()`: Writes contact data to contacts.json
   - `load_contacts()`: Retrieves contact data from contacts.json on startup

2. **⚙️ Contact Management**
   - `add_contact()`: Adds a new contact with name, number, and email
   - `remove_contact()`: Removes a contact by name
   - `show_contact()`: Displays all stored contacts in a formatted view

### 📊 Data Structure

Contacts are stored in the following format:


## 🚀 Usage

1. Run the program
2. Choose from the following options:
   - 1️⃣ Add a new contact
   - 2️⃣ Remove an existing contact
   - 3️⃣ Show all contacts
   - 4️⃣ Exit the program

## 💡 Example


## 🔧 Technical Details

- 🐍 Written in Python
- 📦 Uses the `json` module for data persistence
- ⚠️ Implements error handling for file operations
- 🌐 Global `store` variable for runtime contact storage
- 💾 Automatic data persistence on program exit

## 📁 File Structure

The main program is contained in `update.py` and creates a `contacts.json` file for data storage in the same directory.

---

*Note: This is a basic contact management system suitable for learning purposes and simple contact storage needs.* 🎯

### 👨‍💻 Contributing

Feel free to fork this project and enhance it with new features! 

### 📝 License

Free to use for educational purposes! 

### 🤝 Support

If you have any questions or need help, feel free to open an issue!
# 📞 ContactFlow

<div align="center">
  <img src="Assets/Images/image-03.png" alt="ContactFlow Interface" width="650px"/>
  <p><em>🎯 Modern and intuitive contact management interface showcasing our clean design philosophy and user-centric approach</em></p>
</div>

A seamless contact management system that makes organizing connections effortless. Built with Python, ContactFlow offers intuitive contact handling with persistent storage, making it perfect for both personal and professional use.

## Why ContactFlow?
✨ Fluid user experience
💾 Automatic data persistence (JSON/SQLite)
🔍 Quick contact search
➕ Easy add/remove functionality
📱 Clean command-line interface
🔄 Real-time updates

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

### 📄 License

This project is licensed under the MIT License.

<details>
<summary>View License Text</summary>

MIT License

Copyright (c) 2024 ContactFlow

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
</details>

### 🤝 Support

If you have any questions or need help, feel free to open an issue!
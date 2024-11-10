import tkinter as tk
from tkinter import ttk, messagebox
import json
from ttkthemes import ThemedTk
from PIL import Image, ImageTk
import customtkinter as ctk

class ContactFlowGUI:
    def __init__(self):
        self.window = ThemedTk(theme="arc")  # Modern theme
        self.window.title("ContactFlow")
        self.window.geometry("800x600")
        self.window.configure(bg="#f0f0f0")

        # Initialize store
        self.store = []
        self.load_contacts()

        # Create main containers
        self.create_header()
        self.create_sidebar()
        self.create_main_content()

    def create_header(self):
        # Header frame
        header = tk.Frame(self.window, bg="#2c3e50", height=60)
        header.pack(fill='x')
        
        # App title
        title = tk.Label(
            header,
            text="ContactFlow",
            font=("Helvetica", 20, "bold"),
            bg="#2c3e50",
            fg="white"
        )
        title.pack(pady=10)

    def create_sidebar(self):
        # Sidebar for actions
        sidebar = tk.Frame(self.window, bg="#34495e", width=200)
        sidebar.pack(side='left', fill='y')

        # Action buttons
        actions = [
            ("Add Contact", self.show_add_contact),
            ("View Contacts", self.show_contacts),
            ("Search", self.show_search),
            ("Settings", self.show_settings)
        ]

        for text, command in actions:
            btn = ctk.CTkButton(
                sidebar,
                text=text,
                command=command,
                width=180,
                height=40,
                corner_radius=10,
                fg_color="#3498db",
                hover_color="#2980b9"
            )
            btn.pack(pady=10, padx=10)

    def create_main_content(self):
        # Main content area
        self.main_content = tk.Frame(self.window, bg="#f0f0f0")
        self.main_content.pack(side='right', fill='both', expand=True)

        # Welcome message
        welcome = tk.Label(
            self.main_content,
            text="Welcome to ContactFlow",
            font=("Helvetica", 24),
            bg="#f0f0f0"
        )
        welcome.pack(pady=50)

    def show_add_contact(self):
        # Clear main content
        for widget in self.main_content.winfo_children():
            widget.destroy()

        # Create form
        form_frame = tk.Frame(self.main_content, bg="#f0f0f0")
        form_frame.pack(pady=50)

        fields = ["Name", "Phone", "Email"]
        entries = []

        for field in fields:
            tk.Label(
                form_frame,
                text=field,
                font=("Helvetica", 12),
                bg="#f0f0f0"
            ).pack(pady=5)
            
            entry = ctk.CTkEntry(
                form_frame,
                width=300,
                height=35,
                corner_radius=10
            )
            entry.pack(pady=5)
            entries.append(entry)

        # Save button
        save_btn = ctk.CTkButton(
            form_frame,
            text="Save Contact",
            command=lambda: self.save_contact(entries),
            width=200,
            height=40,
            corner_radius=10,
            fg_color="#27ae60",
            hover_color="#219a52"
        )
        save_btn.pack(pady=20)

    def show_contacts(self):
        # Clear main content
        for widget in self.main_content.winfo_children():
            widget.destroy()

        # Create contacts list
        list_frame = tk.Frame(self.main_content, bg="#f0f0f0")
        list_frame.pack(pady=20, fill='both', expand=True)

        # Contacts table
        columns = ("Name", "Phone", "Email")
        tree = ttk.Treeview(list_frame, columns=columns, show='headings')

        for col in columns:
            tree.heading(col, text=col)
            tree.column(col, width=200)

        for contact in self.store:
            tree.insert("", "end", values=contact)

        tree.pack(pady=20, padx=20)

    def save_contact(self, entries):
        contact = [entry.get() for entry in entries]
        self.store.append(contact)
        self.save_contacts()
        messagebox.showinfo("Success", "Contact saved successfully!")
        self.show_contacts()

    def load_contacts(self):
        try:
            with open("contacts.json", "r") as file:
                self.store = json.load(file)
        except FileNotFoundError:
            self.store = []

    def save_contacts(self):
        with open("contacts.json", "w") as file:
            json.dump(self.store, file)

    def show_search(self):
        # Implement search functionality
        pass

    def show_settings(self):
        # Implement settings functionality
        pass

    def run(self):
        self.window.mainloop()

if __name__ == "__main__":
    app = ContactFlowGUI()
    app.run()

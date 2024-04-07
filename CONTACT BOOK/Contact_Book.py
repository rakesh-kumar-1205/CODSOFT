import tkinter as tk
from tkinter import messagebox
from tkinter import simpledialog
import re

class Contact:
    def __init__(self, name, phone, email, address):
        self.name = name
        self.phone = phone
        self.email = email
        self.address = address

class ContactManagerApp:
    def __init__(self, master):
        self.master = master
        self.master.title("Contact Manager")

        self.contacts = []

        self.name_label = tk.Label(master, text="Name:")
        self.name_label.grid(row=0, column=0, padx=5, pady=5)
        self.name_entry = tk.Entry(master)
        self.name_entry.grid(row=0, column=1, padx=5, pady=5)

        self.phone_label = tk.Label(master, text="Phone:")
        self.phone_label.grid(row=1, column=0, padx=5, pady=5)
        self.phone_entry = tk.Entry(master)
        self.phone_entry.grid(row=1, column=1, padx=5, pady=5)

        self.email_label = tk.Label(master, text="Email:")
        self.email_label.grid(row=2, column=0, padx=5, pady=5)
        self.email_entry = tk.Entry(master)
        self.email_entry.grid(row=2, column=1, padx=5, pady=5)

        self.address_label = tk.Label(master, text="Address:")
        self.address_label.grid(row=3, column=0, padx=5, pady=5)
        self.address_entry = tk.Entry(master)
        self.address_entry.grid(row=3, column=1, padx=5, pady=5)

        self.add_button = tk.Button(master, text="Add Contact", command=self.add_contact)
        self.add_button.grid(row=4, column=0, columnspan=2, padx=5, pady=5)

        self.view_button = tk.Button(master, text="View Contacts", command=self.view_contacts)
        self.view_button.grid(row=5, column=0, columnspan=2, padx=5, pady=5)

        self.search_label = tk.Label(master, text="Search:")
        self.search_label.grid(row=6, column=0, padx=5, pady=5)
        self.search_entry = tk.Entry(master)
        self.search_entry.grid(row=6, column=1, padx=5, pady=5)

        self.search_button = tk.Button(master, text="Search", command=self.search_contact)
        self.search_button.grid(row=7, column=0, columnspan=2, padx=5, pady=5)

        self.delete_button = tk.Button(master, text="Delete Contact", command=self.delete_contact)
        self.delete_button.grid(row=8, column=0, columnspan=2, padx=5, pady=5)

        self.update_button = tk.Button(master, text="Update Contact", command=self.update_contact)
        self.update_button.grid(row=9, column=0, columnspan=2, padx=5, pady=5)

    def add_contact(self):
        try:
            name = self.name_entry.get()
            phone = self.phone_entry.get()
            email = self.email_entry.get()
            address = self.address_entry.get()

            if not name:
                raise ValueError("Name cannot be empty.")
            
            if not re.match(r'^[0-9]{10}$', phone):
                raise ValueError("Invalid phone number format. Please enter a 10-digit number.")
            
            if not re.match(r'^[a-z0-9_.+-]+@[a-z0-9-]+\.[a-z0-9-.]+$', email):
                raise ValueError("Invalid email format.")
            
            # Additional validation for Gmail address
            if not email.endswith('@gmail.com'):
                raise ValueError("Invalid email domain. Please enter a Gmail address.")

            # Check if phone number already exists
            for contact in self.contacts:
                if contact.phone == phone:
                    raise ValueError("Phone number already exists.")

            contact = Contact(name, phone, email, address)
            self.contacts.append(contact)

            messagebox.showinfo("Success", "Contact added successfully.")

            self.clear_entries()
        except ValueError as e:
            messagebox.showerror("Error", str(e))



    def view_contacts(self):
        if not self.contacts:
            messagebox.showinfo("Info", "No contacts available.")
        else:
            contact_list = "\n".join([f"{contact.name} - {contact.phone}" for contact in self.contacts])
            messagebox.showinfo("Contacts", contact_list)

    def search_contact(self):
        try:
            query = self.search_entry.get().strip()
            if not query:
                raise ValueError("Search query cannot be empty.")

            found_contacts = []
            for contact in self.contacts:
                if query.lower() in contact.name.lower() or query in contact.phone:
                    found_contacts.append(contact)

            if not found_contacts:
                messagebox.showinfo("Info", "No matching contacts found.")
            else:
                contact_list = "\n".join([f"{contact.name} - {contact.phone}" for contact in found_contacts])
                messagebox.showinfo("Search Results", contact_list)
        except ValueError as e:
            messagebox.showerror("Error", str(e))

    def delete_contact(self):
        try:
            if not self.contacts:
                raise ValueError("No contacts available.")

            index = simpledialog.askinteger("Delete Contact", "Enter the index of the contact to delete:")
            if index is None:
                return  # User clicked cancel

            index -= 1  # Subtract 1 only if index is not None

            if 0 <= index < len(self.contacts):
                del self.contacts[index]
                messagebox.showinfo("Success", "Contact deleted successfully.")
            else:
                raise ValueError("Invalid index.")
        except ValueError as e:
            messagebox.showerror("Error", str(e))

    def update_contact(self):
        try:
            if not self.contacts:
                raise ValueError("No contacts available.")

            index = simpledialog.askinteger("Update Contact", "Enter the index of the contact to update:")
            if index is None:
                return  # User clicked cancel

            index -= 1  # Subtract 1 only if index is not None

            if 0 <= index < len(self.contacts):
                contact = self.contacts[index]
                contact.name = self.name_entry.get()
                contact.phone = self.phone_entry.get()
                contact.email = self.email_entry.get()
                contact.address = self.address_entry.get()

                messagebox.showinfo("Success", "Contact updated successfully.")
                self.clear_entries()
            else:
                raise ValueError("Invalid index.")
        except ValueError as e:
            messagebox.showerror("Error", str(e))




    def clear_entries(self):
        self.name_entry.delete(0, tk.END)
        self.phone_entry.delete(0, tk.END)
        self.email_entry.delete(0, tk.END)
        self.address_entry.delete(0, tk.END)

def main():
    root = tk.Tk()
    app = ContactManagerApp(root)
    root.mainloop()

if __name__ == "__main__":
    main()

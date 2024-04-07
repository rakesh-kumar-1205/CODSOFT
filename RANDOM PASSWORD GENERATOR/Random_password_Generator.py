import random
import string
import tkinter as tk
from tkinter import messagebox
import pyperclip

def generate_password(length, complexity):
    if complexity == "easy":
        characters = string.ascii_letters + string.digits
    elif complexity == "medium":
        characters = string.ascii_letters + string.digits + string.punctuation.replace("'", "")  # Excluding single quotes
    elif complexity == "strong":
        characters = string.ascii_letters + string.digits + string.punctuation
    else:
        raise ValueError("Invalid complexity level")

    if length < 3:
        raise ValueError("Length should be at least 3 to ensure inclusion of letter, number, and special character.")

    password = random.choice(string.ascii_letters) + random.choice(string.digits) + random.choice(string.punctuation)

    for _ in range(length - 3):
        password += random.choice(characters)

    password_list = list(password)
    random.shuffle(password_list)
    password = ''.join(password_list)

    return password

class PasswordGeneratorApp:
    def __init__(self, master):
        self.master = master
        self.master.title("Password Generator")

        self.length_label = tk.Label(master, text="Length of the Password:")
        self.length_label.grid(row=0, column=0, padx=5, pady=5)
        self.length_entry = tk.Entry(master)
        self.length_entry.grid(row=0, column=1, padx=5, pady=5)

        self.complexity_label = tk.Label(master, text="Complexity:")
        self.complexity_label.grid(row=1, column=0, padx=5, pady=5)
        self.complexity_var = tk.StringVar()
        self.complexity_var.set("easy")
        self.complexity_menu = tk.OptionMenu(master, self.complexity_var, "easy", "medium", "strong")
        self.complexity_menu.grid(row=1, column=1, padx=5, pady=5)

        self.generate_button = tk.Button(master, text="Generate Password", command=self.generate)
        self.generate_button.grid(row=2, column=0, columnspan=2, padx=5, pady=5)

        self.result_label = tk.Label(master, text="")
        self.result_label.grid(row=3, column=0, columnspan=2)

        self.copy_button = tk.Button(master, text="Copy to Clipboard", command=self.copy_to_clipboard)
        self.copy_button.grid(row=4, column=0, columnspan=2, padx=5, pady=5)

    def generate(self):
        try:
            length = int(self.length_entry.get())
            complexity = self.complexity_var.get()
            password = generate_password(length, complexity)
            self.result_label.config(text="Generated Password: " + password)
            self.generated_password = password
        except ValueError as e:
            messagebox.showerror("Error", str(e))
        except Exception as e:
            messagebox.showerror("Error", "An error occurred while generating the password.")

    def copy_to_clipboard(self):
        try:
            pyperclip.copy(self.generated_password)
            messagebox.showinfo("Success", "Password copied to clipboard!")
        except AttributeError:
            messagebox.showerror("Error", "Please generate a password first.")

def main():
    root = tk.Tk()
    app = PasswordGeneratorApp(root)
    root.mainloop()

if __name__ == "__main__":
    main()

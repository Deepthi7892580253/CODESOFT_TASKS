import tkinter as tk
from tkinter import messagebox
import random
import string

def generate_password():
    try:
        length = int(length_entry.get())

        if length <= 0:
            messagebox.showwarning("Warning", "Enter a valid length.")
            return

        characters = ""

        if lowercase.get():
            characters += string.ascii_lowercase

        if uppercase.get():
            characters += string.ascii_uppercase

        if numbers.get():
            characters += string.digits

        if symbols.get():
            characters += string.punctuation

        if characters == "":
            messagebox.showwarning(
                "Warning",
                "Select at least one option."
            )
            return

        password = ""

        for i in range(length):
            password += random.choice(characters)

        password_entry.delete(0, tk.END)
        password_entry.insert(0, password)

    except ValueError:
        messagebox.showerror("Error", "Enter a valid number.")

def copy_password():
    password = password_entry.get()

    if password == "":
        messagebox.showwarning("Warning", "Generate a password first.")
        return

    window.clipboard_clear()
    window.clipboard_append(password)

    messagebox.showinfo("Success", "Password copied!")

def clear():
    length_entry.delete(0, tk.END)
    password_entry.delete(0, tk.END)

window = tk.Tk()
window.title("Password Generator")
window.geometry("500x600")
window.resizable(False, False)
window.configure(bg="#f4f6f8")

tk.Label(
    window,
    text="PASSWORD GENERATOR",
    font=("Arial", 24, "bold"),
    bg="#f4f6f8"
).pack(pady=(30, 5))

tk.Label(
    window,
    text="Create a strong random password",
    font=("Arial", 11),
    bg="#f4f6f8",
    fg="#666666"
).pack()

tk.Label(
    window,
    text="Password Length",
    font=("Arial", 12, "bold"),
    bg="#f4f6f8"
).pack(pady=(30, 5))

length_entry = tk.Entry(
    window,
    font=("Arial", 14),
    width=15,
    justify="center"
)
length_entry.pack(ipady=7)

lowercase = tk.BooleanVar(value=True)
uppercase = tk.BooleanVar(value=True)
numbers = tk.BooleanVar(value=True)
symbols = tk.BooleanVar(value=True)

tk.Checkbutton(
    window,
    text="Lowercase (a-z)",
    variable=lowercase,
    bg="#f4f6f8"
).pack()

tk.Checkbutton(
    window,
    text="Uppercase (A-Z)",
    variable=uppercase,
    bg="#f4f6f8"
).pack()

tk.Checkbutton(
    window,
    text="Numbers (0-9)",
    variable=numbers,
    bg="#f4f6f8"
).pack()

tk.Checkbutton(
    window,
    text="Symbols (!@#$)",
    variable=symbols,
    bg="#f4f6f8"
).pack()

tk.Button(
    window,
    text="GENERATE PASSWORD",
    font=("Arial", 11, "bold"),
    width=22,
    command=generate_password
).pack(pady=20)

password_entry = tk.Entry(
    window,
    font=("Arial", 14),
    width=32,
    justify="center"
)
password_entry.pack(ipady=8)

tk.Button(
    window,
    text="COPY PASSWORD",
    width=18,
    command=copy_password
).pack(pady=15)

tk.Button(
    window,
    text="CLEAR",
    width=15,
    command=clear
).pack()

tk.Label(
    window,
    text="",
    font=("Arial", 9),
    bg="#f4f6f8",
    fg="#888888"
).pack(side="bottom", pady=15)

window.mainloop()
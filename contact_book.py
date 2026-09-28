import tkinter as tk
from tkinter import messagebox

contacts = {}

def clear_fields():
    name_entry.delete(0, tk.END)
    phone_entry.delete(0, tk.END)
    email_entry.delete(0, tk.END)
    address_entry.delete(0, tk.END)

def add_contact():
    name = name_entry.get().strip()
    phone = phone_entry.get().strip()
    email = email_entry.get().strip()
    address = address_entry.get().strip()

    if name == "":
        messagebox.showwarning("Warning", "Please enter a name.")
        return

    contacts[name] = {
        "phone": phone,
        "email": email,
        "address": address
    }

    show_contacts()
    clear_fields()

def show_contacts():
    contact_list.delete(0, tk.END)

    for name, details in contacts.items():
        contact_list.insert(
            tk.END,
            name + " | " + details["phone"]
        )

def select_contact(event=None):
    selected = contact_list.curselection()

    if not selected:
        return

    text = contact_list.get(selected[0])
    name = text.split(" | ")[0]

    details = contacts[name]

    clear_fields()

    name_entry.insert(0, name)
    phone_entry.insert(0, details["phone"])
    email_entry.insert(0, details["email"])
    address_entry.insert(0, details["address"])

def update_contact():
    selected = contact_list.curselection()

    if not selected:
        messagebox.showwarning(
            "Warning",
            "Select a contact to update."
        )
        return

    old_text = contact_list.get(selected[0])
    old_name = old_text.split(" | ")[0]

    new_name = name_entry.get().strip()
    phone = phone_entry.get().strip()
    email = email_entry.get().strip()
    address = address_entry.get().strip()

    if new_name == "":
        messagebox.showwarning(
            "Warning",
            "Name cannot be empty."
        )
        return

    del contacts[old_name]

    contacts[new_name] = {
        "phone": phone,
        "email": email,
        "address": address
    }

    show_contacts()
    clear_fields()

def delete_contact():
    selected = contact_list.curselection()

    if not selected:
        messagebox.showwarning(
            "Warning",
            "Select a contact to delete."
        )
        return

    text = contact_list.get(selected[0])
    name = text.split(" | ")[0]

    del contacts[name]

    show_contacts()
    clear_fields()

def search_contact():
    search = search_entry.get().strip().lower()

    contact_list.delete(0, tk.END)

    for name, details in contacts.items():

        if (
            search in name.lower()
            or search in details["phone"]
        ):
            contact_list.insert(
                tk.END,
                name + " | " + details["phone"]
            )

def show_all():
    search_entry.delete(0, tk.END)
    show_contacts()

window = tk.Tk()
window.title("Contact Book")
window.geometry("650x700")
window.resizable(False, False)
window.configure(bg="#f4f6f8")

tk.Label(
    window,
    text="CONTACT BOOK",
    font=("Arial", 26, "bold"),
    bg="#f4f6f8"
).pack(pady=(25, 5))

tk.Label(
    window,
    text="Manage your contacts easily",
    font=("Arial", 11),
    bg="#f4f6f8",
    fg="#666666"
).pack()

input_frame = tk.Frame(window, bg="#f4f6f8")
input_frame.pack(pady=20)

tk.Label(
    input_frame,
    text="Name:",
    bg="#f4f6f8"
).grid(row=0, column=0, padx=10, pady=7)

name_entry = tk.Entry(
    input_frame,
    width=35
)
name_entry.grid(row=0, column=1)

tk.Label(
    input_frame,
    text="Phone:",
    bg="#f4f6f8"
).grid(row=1, column=0, padx=10, pady=7)

phone_entry = tk.Entry(
    input_frame,
    width=35
)
phone_entry.grid(row=1, column=1)

tk.Label(
    input_frame,
    text="Email:",
    bg="#f4f6f8"
).grid(row=2, column=0, padx=10, pady=7)

email_entry = tk.Entry(
    input_frame,
    width=35
)
email_entry.grid(row=2, column=1)

tk.Label(
    input_frame,
    text="Address:",
    bg="#f4f6f8"
).grid(row=3, column=0, padx=10, pady=7)

address_entry = tk.Entry(
    input_frame,
    width=35
)
address_entry.grid(row=3, column=1)

tk.Button(
    window,
    text="ADD CONTACT",
    width=18,
    command=add_contact
).pack(pady=8)

search_frame = tk.Frame(window, bg="#f4f6f8")
search_frame.pack(pady=15)

search_entry = tk.Entry(
    search_frame,
    width=30
)
search_entry.grid(row=0, column=0, padx=5)

tk.Button(
    search_frame,
    text="SEARCH",
    command=search_contact
).grid(row=0, column=1, padx=5)

tk.Button(
    search_frame,
    text="SHOW ALL",
    command=show_all
).grid(row=0, column=2, padx=5)

contact_list = tk.Listbox(
    window,
    font=("Arial", 12),
    width=55,
    height=10
)
contact_list.pack(pady=10)

contact_list.bind(
    "<<ListboxSelect>>",
    select_contact
)

button_frame = tk.Frame(window, bg="#f4f6f8")
button_frame.pack(pady=15)

tk.Button(
    button_frame,
    text="UPDATE",
    width=12,
    command=update_contact
).grid(row=0, column=0, padx=5)

tk.Button(
    button_frame,
    text="DELETE",
    width=12,
    command=delete_contact
).grid(row=0, column=1, padx=5)

tk.Button(
    button_frame,
    text="CLEAR",
    width=12,
    command=clear_fields
).grid(row=0, column=2, padx=5)

tk.Label(
    window,
    text="",
    font=("Arial", 9),
    bg="#f4f6f8",
    fg="#888888"
).pack(side="bottom", pady=12)

window.mainloop()
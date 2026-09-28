import tkinter as tk
from tkinter import messagebox

def add_task():
    task = task_entry.get().strip()

    if task == "":
        messagebox.showwarning("Warning", "Please enter a task.")
        return

    task_list.insert(tk.END, task)
    task_entry.delete(0, tk.END)

def select_task(event=None):
    selected = task_list.curselection()

    if selected:
        task = task_list.get(selected[0])

        # Remove completed symbol while editing
        if task.startswith("✓ "):
            task = task[2:]

        task_entry.delete(0, tk.END)
        task_entry.insert(0, task)


# -----------------------------
# Update Task
# -----------------------------
def update_task():

    selected = task_list.curselection()

    if not selected:
        messagebox.showwarning(
            "Warning",
            "Please select a task to update."
        )
        return

    new_task = task_entry.get().strip()

    if new_task == "":
        messagebox.showwarning(
            "Warning",
            "Please enter the updated task."
        )
        return

    # Get selected task position
    position = selected[0]

    # Delete old task
    task_list.delete(position)

    # Insert updated task at same position
    task_list.insert(position, new_task)

    # Select the updated task
    task_list.selection_set(position)

    # Clear input box
    task_entry.delete(0, tk.END)

    messagebox.showinfo(
        "Success",
        "Task updated successfully!"
    )


# -----------------------------
# Complete Task
# -----------------------------
def complete_task():

    selected = task_list.curselection()

    if not selected:
        messagebox.showwarning(
            "Warning",
            "Please select a task."
        )
        return

    position = selected[0]
    task = task_list.get(position)

    # Don't add ✓ twice
    if not task.startswith("✓ "):

        task_list.delete(position)
        task_list.insert(position, "✓ " + task)

        task_list.selection_set(position)


# -----------------------------
# Delete Task
# -----------------------------
def delete_task():

    selected = task_list.curselection()

    if not selected:
        messagebox.showwarning(
            "Warning",
            "Please select a task to delete."
        )
        return

    position = selected[0]

    task_list.delete(position)

    task_entry.delete(0, tk.END)


def clear_all():

    if task_list.size() == 0:
        messagebox.showinfo(
            "Information",
            "There are no tasks to clear."
        )
        return

    answer = messagebox.askyesno(
        "Confirm",
        "Do you want to delete all tasks?"
    )

    if answer:
        task_list.delete(0, tk.END)
        task_entry.delete(0, tk.END)


window = tk.Tk()

window.title("My To-Do List")
window.geometry("550x650")
window.resizable(False, False)

window.configure(bg="#f4f6f8")


title = tk.Label(
    window,
    text="MY TO-DO LIST",
    font=("Arial", 26, "bold"),
    bg="#f4f6f8",
    fg="#222222"
)

title.pack(pady=(25, 5))


subtitle = tk.Label(
    window,
    text="Add, update and manage your tasks",
    font=("Arial", 11),
    bg="#f4f6f8",
    fg="#666666"
)

subtitle.pack()


task_entry = tk.Entry(
    window,
    font=("Arial", 14),
    width=38,
    bd=2,
    relief="solid"
)

task_entry.pack(
    pady=(25, 10),
    ipady=8
)


add_button = tk.Button(
    window,
    text="ADD TASK",
    font=("Arial", 11, "bold"),
    width=18,
    command=add_task
)

add_button.pack(pady=5)


task_list = tk.Listbox(
    window,
    font=("Arial", 13),
    width=45,
    height=13,
    bd=2,
    relief="solid",
    selectmode=tk.SINGLE
)

task_list.pack(pady=20)


# When user clicks a task,
# automatically show it in entry box
task_list.bind(
    "<<ListboxSelect>>",
    select_task
)


button_frame = tk.Frame(
    window,
    bg="#f4f6f8"
)

button_frame.pack()


update_button = tk.Button(
    button_frame,
    text="UPDATE",
    width=11,
    font=("Arial", 10, "bold"),
    command=update_task
)

update_button.grid(
    row=0,
    column=0,
    padx=5
)


complete_button = tk.Button(
    button_frame,
    text="COMPLETE",
    width=11,
    font=("Arial", 10, "bold"),
    command=complete_task
)

complete_button.grid(
    row=0,
    column=1,
    padx=5
)


delete_button = tk.Button(
    button_frame,
    text="DELETE",
    width=11,
    font=("Arial", 10, "bold"),
    command=delete_task
)

delete_button.grid(
    row=0,
    column=2,
    padx=5
)


clear_button = tk.Button(
    window,
    text="CLEAR ALL",
    width=18,
    font=("Arial", 10, "bold"),
    command=clear_all
)

clear_button.pack(pady=15)



instruction = tk.Label(
    window,
    text="Click a task to edit it, then press UPDATE",
    font=("Arial", 10),
    bg="#f4f6f8",
    fg="#777777"
)

instruction.pack()


footer = tk.Label(
    window,
    text="",
    font=("Arial", 9),
    bg="#f4f6f8",
    fg="#888888"
)

footer.pack(
    side="bottom",
    pady=12
)

window.mainloop()
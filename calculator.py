import tkinter as tk
from tkinter import messagebox

def calculate():
    try:
        num1 = float(first_number.get())
        num2 = float(second_number.get())
        operation = operation_box.get()

        if operation == "Addition (+)":
            result = num1 + num2

        elif operation == "Subtraction (-)":
            result = num1 - num2

        elif operation == "Multiplication (*)":
            result = num1 * num2

        elif operation == "Division (/)":
            if num2 == 0:
                messagebox.showerror("Error", "Cannot divide by zero.")
                return
            result = num1 / num2

        else:
            messagebox.showwarning("Warning", "Select an operation.")
            return

        result_label.config(text="Result = " + str(result))

    except ValueError:
        messagebox.showerror("Error", "Enter valid numbers.")

def clear():
    first_number.delete(0, tk.END)
    second_number.delete(0, tk.END)
    operation_box.set("Select Operation")
    result_label.config(text="Result = ")

window = tk.Tk()
window.title("Simple Calculator")
window.geometry("450x550")
window.resizable(False, False)
window.configure(bg="#f4f6f8")

tk.Label(
    window,
    text="SIMPLE CALCULATOR",
    font=("Arial", 24, "bold"),
    bg="#f4f6f8"
).pack(pady=(30, 5))

tk.Label(
    window,
    text="Perform basic calculations easily",
    font=("Arial", 11),
    bg="#f4f6f8",
    fg="#666666"
).pack()

tk.Label(
    window,
    text="First Number",
    font=("Arial", 12, "bold"),
    bg="#f4f6f8"
).pack(pady=(30, 5))

first_number = tk.Entry(
    window,
    font=("Arial", 14),
    width=25,
    justify="center"
)
first_number.pack(ipady=7)

tk.Label(
    window,
    text="Second Number",
    font=("Arial", 12, "bold"),
    bg="#f4f6f8"
).pack(pady=(20, 5))

second_number = tk.Entry(
    window,
    font=("Arial", 14),
    width=25,
    justify="center"
)
second_number.pack(ipady=7)

tk.Label(
    window,
    text="Operation",
    font=("Arial", 12, "bold"),
    bg="#f4f6f8"
).pack(pady=(20, 5))

operation_box = tk.StringVar()
operation_box.set("Select Operation")

operations = [
    "Addition (+)",
    "Subtraction (-)",
    "Multiplication (*)",
    "Division (/)"
]

tk.OptionMenu(
    window,
    operation_box,
    *operations
).pack()

tk.Button(
    window,
    text="CALCULATE",
    font=("Arial", 11, "bold"),
    width=18,
    command=calculate
).pack(pady=25)

result_label = tk.Label(
    window,
    text="Result = ",
    font=("Arial", 18, "bold"),
    bg="#f4f6f8"
)
result_label.pack()

tk.Button(
    window,
    text="CLEAR",
    width=15,
    command=clear
).pack(pady=20)

tk.Label(
    window,
    text="",
    font=("Arial", 9),
    bg="#f4f6f8",
    fg="#888888"
).pack(side="bottom", pady=15)

window.mainloop()
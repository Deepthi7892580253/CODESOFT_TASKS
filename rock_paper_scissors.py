import tkinter as tk
import random

user_score = 0
computer_score = 0
tie_score = 0

choices = ["Rock", "Paper", "Scissors"]

def play(choice):
    global user_score
    global computer_score
    global tie_score

    computer = random.choice(choices)

    user_choice_label.config(
        text="You chose: " + choice
    )

    computer_choice_label.config(
        text="Computer chose: " + computer
    )

    if choice == computer:
        result_label.config(text="IT'S A TIE!")
        tie_score += 1

    elif (
        (choice == "Rock" and computer == "Scissors")
        or
        (choice == "Paper" and computer == "Rock")
        or
        (choice == "Scissors" and computer == "Paper")
    ):
        result_label.config(text="YOU WIN!")
        user_score += 1

    else:
        result_label.config(text="COMPUTER WINS!")
        computer_score += 1

    score_label.config(
        text="Your Score: " + str(user_score)
        + "    Computer Score: " + str(computer_score)
        + "    Ties: " + str(tie_score)
    )

def reset():
    global user_score
    global computer_score
    global tie_score

    user_score = 0
    computer_score = 0
    tie_score = 0

    user_choice_label.config(text="You chose:")
    computer_choice_label.config(text="Computer chose:")
    result_label.config(text="Choose Rock, Paper or Scissors")
    score_label.config(
        text="Your Score: 0    Computer Score: 0    Ties: 0"
    )

window = tk.Tk()
window.title("Rock Paper Scissors")
window.geometry("550x600")
window.resizable(False, False)
window.configure(bg="#f4f6f8")

tk.Label(
    window,
    text="ROCK PAPER SCISSORS",
    font=("Arial", 24, "bold"),
    bg="#f4f6f8"
).pack(pady=(30, 5))

tk.Label(
    window,
    text="Choose your move!",
    font=("Arial", 11),
    bg="#f4f6f8",
    fg="#666666"
).pack()

button_frame = tk.Frame(window, bg="#f4f6f8")
button_frame.pack(pady=35)

tk.Button(
    button_frame,
    text="ROCK",
    width=12,
    height=2,
    command=lambda: play("Rock")
).grid(row=0, column=0, padx=5)

tk.Button(
    button_frame,
    text="PAPER",
    width=12,
    height=2,
    command=lambda: play("Paper")
).grid(row=0, column=1, padx=5)

tk.Button(
    button_frame,
    text="SCISSORS",
    width=12,
    height=2,
    command=lambda: play("Scissors")
).grid(row=0, column=2, padx=5)

user_choice_label = tk.Label(
    window,
    text="You chose:",
    font=("Arial", 14, "bold"),
    bg="#f4f6f8"
)
user_choice_label.pack(pady=10)

computer_choice_label = tk.Label(
    window,
    text="Computer chose:",
    font=("Arial", 14, "bold"),
    bg="#f4f6f8"
)
computer_choice_label.pack(pady=10)

result_label = tk.Label(
    window,
    text="Choose Rock, Paper or Scissors",
    font=("Arial", 20, "bold"),
    bg="#f4f6f8"
)
result_label.pack(pady=30)

score_label = tk.Label(
    window,
    text="Your Score: 0    Computer Score: 0    Ties: 0",
    font=("Arial", 11, "bold"),
    bg="#f4f6f8"
)
score_label.pack()

tk.Button(
    window,
    text="RESET GAME",
    width=15,
    command=reset
).pack(pady=25)

tk.Label(
    window,
    text="",
    font=("Arial", 9),
    bg="#f4f6f8",
    fg="#888888"
).pack(side="bottom", pady=15)

window.mainloop()
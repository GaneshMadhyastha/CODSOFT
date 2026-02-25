import random
from tkinter import *
from tkinter import messagebox

#Global Vriables for score tracking
user_score=0
computer_score=0
choices=["rock","paper","scissors"]

def player(user_choice):
    #code game logic 
    global user_score,computer_score
    computer_choice=random.choice(choices)

    #determine the winner based on logic
    if user_choice == computer_choice:
        result="IT'S A TIE!"
        result_color="black"
    elif(user_choice=="rock" and computer_choice=="scissors")or\
        (user_choice == "scissors" and computer_choice == "paper") or \
        (user_choice == "paper" and computer_choice == "rock"):
        result = "YOU WIN!!"
        result_color="#2e7d32"
        user_score+=1
    else:
        result = "YOU LOSE!!"
        result_color="#e7305b"
        computer_score+=1

    #Display Result
    choice_label.config(text=f"YOU: {user_choice.upper()}  vs  CPU: {computer_choice.upper()}")
    result_label.config(text=f"RESULT: {result}", fg=result_color)
    score_label.config(text=f"You: {user_score} | Computer: {computer_score}")

def reset_game():
    #feature to reset scores
    global user_score,computer_score
    user_score=0
    computer_score=0
    score_label.config(text="You : 0 | computer: 0")
    result_label.config(text="---",fg="black")
    choice_label.config(text="Choose your movie!")

#GUI Setup
BG_COLOR = "skyblue"
BTN_PURPLE = "#9000a0"

root = Tk()
root.title("CODSOFT Rock-Paper-Scissors")
root.geometry("500x450")
root.config(padx=20, pady=20, bg=BG_COLOR)

# Header
Label(root, text="Rock-Paper-Scissors", font=("Courier", 22, "bold"), bg=BG_COLOR).pack(pady=10)

# Scoreboard Section
score_label = Label(root, text="You: 0 | Computer: 0", font=("Courier", 14, "bold"), 
                    bg="white", relief="solid", pady=5)
score_label.pack(fill=X, pady=10)

choice_label = Label(root, text="Choose your move!", font=("Courier", 12), bg=BG_COLOR)
choice_label.pack(pady=10)

# Button Frame for Player Choices
btn_frame = Frame(root, bg=BG_COLOR)
btn_frame.pack(pady=10)

# Creating buttons 
Button(btn_frame, text="Rock", width=10, bg=BTN_PURPLE, fg="white", font=("bold"),
       command=lambda: player("rock")).grid(row=0, column=0, padx=5)

Button(btn_frame, text="Paper", width=10, bg=BTN_PURPLE, fg="white", font=("bold"),
       command=lambda: player("paper")).grid(row=0, column=1, padx=5)

Button(btn_frame, text="Scissors", width=10, bg=BTN_PURPLE, fg="white", font=("bold"),
       command=lambda: player("scissors")).grid(row=0, column=2, padx=5)

#Result Display
result_label = Label(root, text="---", font=("Courier", 18, "bold"), bg=BG_COLOR)
result_label.pack(pady=25)

#Exit and Reset Buttons
Button(root, text="Reset Scores", command=reset_game, bg="white").pack(side=LEFT, padx=10)
Button(root, text="Exit Game", command=root.quit, bg="white").pack(side=RIGHT, padx=10)

root.mainloop()
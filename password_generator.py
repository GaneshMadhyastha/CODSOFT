import random
import string
from tkinter import *
from tkinter import messagebox

def generate_password():
    #function to generate random password based on user provided length
    all_chars = string.ascii_letters + string.digits + string.punctuation
    try:
        #retrieve length from entry widget
        length = int(length_entry.get())
        #Validation:ensure length is within a reasonable range
        if length <= 0:
            messagebox.showwarning("Error", "Length must be at least 1.")
        elif length > 100:
            messagebox.showwarning("Error", "Please keep password under 100 characters.")
        else:
            #randomly select 'k' characters form the pool and join them into a string
            password = ''.join(random.choices(all_chars, k=length))
            #update the result on GUI with new pass
            result_label.config(text=f"Generated Password: {password}", fg="#2e7d32")
    except ValueError:
        #Handle cases where input is not valid example text or empty
        messagebox.showerror("Error", "Please enter a valid whole number.")
        
 #Background color       
BG_COLOR="skyblue"
BTN_COLOR = "#9000a0"

# GUI Setup
root = Tk()
root.title("CODSOFT Password Generator")
root.geometry("500x300")
root.config(padx=20, pady=20,bg=BG_COLOR)
#Title Heading
title_label = Label(text="Password Generator", font=("Courier", 24, "bold"),bg=BG_COLOR)
title_label.pack(pady=10)
#Instruction Label
instr_label = Label(text="Enter the desired length of the password:", font=("Courier", 12),bg=BG_COLOR)
instr_label.pack()
#Input Failed or Pass length
length_entry = Entry(font=("Courier", 15), width=11)
length_entry.pack(pady=10)
length_entry.insert(0, "12")#default length
#Button for Pass generation
gen_button = Button(text="Generate Password", command=generate_password, bg=BTN_COLOR, fg="white", font=("Courier", 12, "bold"))
gen_button.pack(pady=10)
#Display Result
result_label = Label(text="", font=("Courier", 11, "bold"), wraplength=400,bg=BG_COLOR)
result_label.pack(pady=25)

#start tkinter event loop
root.mainloop()
  
import tkinter as tk
from tkinter import messagebox
import random 

def check_guess():
    global number_to_guess, guess_counter

    try:
        my_guess = int(entry_guess.get())
    except ValueError:
        messagebox.sowerror("Invalid  input","Please Enter a Valid Number . " )
        return
    
    guess_counter += 1

    if my_guess == number_to_guess:

        messagebox.showinfo("Congratulations!", f"The number was {number_to_guess}. You found it in {guess_counter} attempts!")
        reset_game()
    elif guess_counter >= chances:
        messagebox.showinfo("Game Over", f"Oops! The number was {number_to_guess} . Better Luck Next Time!")
        reset_game()
    elif my_guess > number_to_guess:
        label_feedback.config(text="Your Guess is too high . ")
    elif my_guess < number_to_guess:
        label_feedback.config(text="Your Guess is low . ")
    
def reset_game():
    global number_to_guess, guess_counter
    number_to_guess =random.randrange(100)
    guess_counter = 0
    label_feedback.config(text="Guess a number between 0 to 100 .")
#Create the main window.....
    
root=tk.Tk()
root.title("Number Guessing Game")
root.geometry("500x350")
root.configure(bg="#f0f8ff")

#title frame 

frame_title = tk.Frame(root,bg="#4682b4")
frame_title.pack(pady=10 , fill=tk.X)

label_title = tk.Label(frame_title, text="Number Guessing Game", font=("Helvetica", 16, "bold"), bg="#4682b4", fg="white")
label_title.pack(pady=10)

#instruction frame

frame_instruction = tk.Frame(root, bg="#e6e6fa")  # Lavender background
frame_instruction.pack(pady=10, fill=tk.X)

label_instruction = tk.Label(frame_instruction, text="Guess the number between 0 and 100.", font=("Helvetica", 14), bg="#e6e6fa")
label_instruction.pack(pady=10)

# Entry and Button Frame
frame_entry_button = tk.Frame(root, bg="#ffffff")  # White background
frame_entry_button.pack(pady=10)

entry_guess = tk.Entry(frame_entry_button, font=("Helvetica", 14), width=10, borderwidth=2, relief="groove")
entry_guess.pack(side=tk.LEFT, padx=10)

button_submit = tk.Button(frame_entry_button, text="Submit Guess", font=("Helvetica", 14), command=check_guess, bg="#32cd32", fg="white", relief="raised")
button_submit.pack(side=tk.LEFT, padx=10)

# Feedback Label
label_feedback = tk.Label(root, text="Guess a number between 0 and 100.", font=("Helvetica", 14), bg="#ffffff")
label_feedback.pack(pady=20)

# Initialize game variables
number_to_guess = random.randrange(100)
guess_counter = 0
chances = 10

# Run the main event loop
root.mainloop()
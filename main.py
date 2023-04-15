import tkinter as tk
from q_codes import qc

user_input = "Q"

def keyup(e):
    # https://stackoverflow.com/questions/27215326/tkinter-keypress-and-keyrelease-events
    # used key release event, press event doesn't matter... don't want to catch key repeat
    global user_input
    if e.keysym == "BackSpace" and len(user_input)>1:
        user_input = user_input[:-1]
    elif e.keysym == "Escape":
        user_input = "Q"
    else:
        if len(user_input) <3:
            user_input += e.char.upper()
    in_label.config(text=user_input, font=('Arial', 50))


root = tk.Tk()
root.title("Q-Lookup by KI5WWP")
in_frame = tk.Frame(root, width = 300, height = 45, highlightbackground="blue", highlightthickness=2)
frame = tk.Frame(root, width=300, height=300)
in_label = tk.Label(in_frame, text = user_input, font=('Arial', 50))
in_label.pack()

#frame.bind("<KeyPress>", keydown)
frame.bind("<KeyRelease>", keyup)

in_frame.pack()
frame.pack()

frame.focus_set()
root.mainloop()
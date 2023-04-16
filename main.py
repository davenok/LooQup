import tkinter as tk
from q_codes import qc

user_input = "Q"
instruction = "Q-Lookup\nA utility to help with those crazy Q Codes.\nby KI5WWP\n\n"
instruction += "Start typing the Q-code (the Q is already there)\n\n"
instruction += "KEYS:\n<BACKSPACE> --- backspaces\n<ESC> --- Clears all input - start again"
instruction += "\n<ALT>+<F4> --- Exit the program"
out_text = instruction

def update_output():
    global out_text
    # out_text = user_input
    l = len(user_input)
    matches = ""
    my_match = ""
    if len(user_input) == 2:
        for d in qc:
            if d["code"][0:l] == user_input:
                if not matches == "":
                    matches += ", "
                matches += d["code"]
        if len(matches) == 0:
            matches = "Sorry, no matches found."
        out_text = matches
        # print(matches)
    elif len(user_input) == 3:
        for d in qc:
            if d["code"] == user_input:
                my_match = d["statement"]
        # print(my_match)
        if len(my_match) == 0:
            out_text = "Sorry, no match found."
        else:
            out_text = my_match

    out_label.config(text= out_text)
    out_label.pack()

def keyup(e):
    # https://stackoverflow.com/questions/27215326/tkinter-keypress-and-keyrelease-events
    # used key release event, press event doesn't matter... don't want to catch key repeat
    global user_input
    global out_text
    if e.keysym == "BackSpace" and len(user_input)>1:
        user_input = user_input[:-1]
        if len(user_input) == 1:
            out_label.config(text = instruction)
            out_label.pack()
        else:
            update_output()
    elif e.keysym == "Escape":
        user_input = "Q"
        out_label.config(text = instruction)
        out_label.pack()
    
    else:
        if len(user_input) <3 and e.char in "abcdefghijklmnopqrstuvwxyz":
            user_input += e.char.upper()
            update_output()
    in_label.config(text=user_input, font=('Arial', 50))

# Q-Lookup in tkinter
root = tk.Tk()
root.title("Q-Lookup by KI5WWP")
#root.geometry("440x320")
in_frame = tk.Frame(root, width = 300, height = 45)
in_label = tk.Label(in_frame, text = user_input, font=('Arial', 50)
    , highlightbackground="blue", highlightthickness=3)
out_label = tk.Label(in_frame, text = out_text)
in_label.pack()
out_label.pack()
in_frame.bind("<KeyRelease>", keyup)
in_frame.pack()
in_frame.focus_set()
root.mainloop()
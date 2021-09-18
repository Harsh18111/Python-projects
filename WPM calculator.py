import random
from tkinter import *
import time
from typing import get_origin

root = Tk()
root.title("WPM test")

# random quote gen
q_1 = "Envy of other people shows how they are unhappy. Their continual attention to others behavior shows how they are boring."
q_2 = "Beware the stories you read or tell; subtly, at night, beneath the waters of consciousness, they are altering your world."
quotes = [q_1, q_2]
q = random.choice(quotes)
q_prin = Label(root, text=q, font=("Arial", 15))
q_prin.grid(row=0, column=0)

# functions
def start():
    global e
    e = Entry(root, width=105, borderwidth=5, font=("Arial", 15))
    e.grid(row=1, column=0)
    global go
    go = time.time()

def stop():
    if e == q_1 or q_2:
        e.config(state=DISABLED)
        end = time.time()
        global t
        t = end - go
        global wpm
        wpm = 20/t
        f_wpm = "Your WPM is:", wpm
        ans = Label(root, text=f_wpm, font=("Arial", 20))
        ans.grid(row=5, column=0)
    else:
        no = Label(root, text="Error", font=("Arial", 20))
        no.grid(row=4, column=0)


# start button
start_btn = Button(root, text="START", padx=30, pady=10, command=lambda: start())
start_btn.grid(row=2, column=0)

# stop btn
stop_btn = Button(root, text="STOP", padx=30, pady=10, command=lambda: stop())
stop_btn.grid(row=3, column=0)

root.mainloop()
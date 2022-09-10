from tkinter import *
import datetime
START_TIME = 0


def reset_timer():
    global START_TIME
    START_TIME = 0
    timer_label.config(text="")
    timer()


def timer():
    global START_TIME
    if START_TIME == 0:
        START_TIME = datetime.datetime.now()
    elapsed = datetime.datetime.now() - START_TIME
    elapsed = int(str(elapsed).split(".")[0].split(":")[-1])
    countdown = 9 - elapsed
    if countdown > 0:
        timer_label.config(text=f"Time remaining:{str(countdown)} Seconds")
        root.after(1000, timer)
    else:
        timer_label.config(text="Time Up. All Delete")
        text.delete(1.0, END)
        reset_timer()


def key_pressed(event):
    reset_timer()


# Make the UI
root = Tk()
root.title("Disappearing Text Writing App")
root.minsize(width=800, height=600)

instruction1_label = Label(root, pady=20, text="For most writers, a big problem is writing block. Where you can't think of what to write and you can't write anything.\n "
                                               "One of the most interesting solutions to this is Disappearing Test app, where if you do not type for 10 seconds, then all text will disappear.")
instruction1_label.pack()

# Timer
timer_label = Label(root, pady=20, padx=20, text="")
timer_label.pack()

# Box to type
text = Text(root, width=100)
text.focus()
text.bind("<Key>", key_pressed)
text.pack(pady=50)

root.after(1000, timer)
root.mainloop()

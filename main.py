from tkinter import *
import math
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#cc0e74"
RED = "#e7305b"
GREEN = "#94fc13"
YELLOW = "#f7f5dd"
DARK = "#060930"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps = 0
timer = None
# ---------------------------- TIMER RESET ------------------------------- # 
def reset_timer():
    window.after_cancel(timer)
    time.config(text="00:00")
    title_label.config(text="Timer")
    tick_label.config(text="")
# ---------------------------- TIMER MECHANISM ------------------------------- # 
def start_timer():
    global reps
    reps += 1
    work_sec = WORK_MIN * 60
    short_break_sec = SHORT_BREAK_MIN * 60
    long_break_sec = LONG_BREAK_MIN * 60
    if reps % 8 == 0:
        count_down(long_break_sec)
        title_label.config(text="Long Break", fg=PINK)
    elif reps % 2 == 0:
        count_down(short_break_sec)
        title_label.config(text="Break", fg=YELLOW)
    else:
        count_down(work_sec)
        title_label.config(text="Work", fg=RED)



# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 
def count_down(count):

    count_min = math.floor(count / 60)
    count_sec = count % 60
    if count_sec < 10:
        count_sec = f"0{count_sec}"
    time.config(time, text=f"{count_min}:{count_sec}")
    if count > 0:
        global timer
        timer = window.after(1000, count_down, count - 1)
    else:
        start_timer()
        mark = ""
        work_sessions = math.floor(reps/2)
        for _ in range(work_sessions):
            mark += "✔"
            tick_label.config(text=mark)


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Pomodoro")
window.config(padx=100, pady=50, bg=DARK)


canvas = Canvas(width=670, height=840, bg=DARK, highlightthickness=0)
yoda_img = PhotoImage(file="baby_yoda.png")
canvas.create_image(335, 420, image=yoda_img)
canvas.grid(column=2, row=2)

title_label = Label(text="Timer", font=("Ariel", 59, "bold"))
title_label.grid(column=0, row=0, sticky="n")
title_label.config(padx=5, pady=5, fg=GREEN, bg=DARK)

time = Label(text="00:00", font=(FONT_NAME, 54, "bold"))
time.grid(column=2, row=0)
time.config(fg=GREEN, bg=DARK)

start_button = Button(text="Start", width=10, height=5, command=start_timer)
start_button.grid(column=1, row=0, sticky="nnw")
reset_button = Button(text="Reset", width=10, height=5, command=reset_timer)
reset_button.grid(column=1, row=1)

tick_label = Label()
tick_label.grid(column=0, row=1)
tick_label.config(padx=5, pady=5, fg=GREEN, bg=DARK)




window.mainloop()

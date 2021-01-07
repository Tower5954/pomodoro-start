from tkinter import *
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

# ---------------------------- TIMER RESET ------------------------------- # 

# ---------------------------- TIMER MECHANISM ------------------------------- # 

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 

# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Pomodoro")
window.config(padx=100, pady=50, bg=DARK)

canvas = Canvas(width=670, height= 840, bg=DARK, highlightthickness=0)
yoda_img = PhotoImage(file="baby_yoda.png")
canvas.create_image(320, 400, image=yoda_img)
canvas.create_text(335, 320, text="00:00", fill=YELLOW,  font=(FONT_NAME, 54, "bold"))
canvas.grid(column=2, row=0)

timer_label = Label(text="Timer", font=("Ariel", 59, "bold"))
timer_label.grid(column=0, row=0, sticky= "n")
timer_label.config(padx=5, pady=5, fg=GREEN, bg=DARK)

button = Button(text="Start", width=10, height=5)
button.grid(column=1, row=0, sticky="nnw")
button_2 = Button(text="Finish", width=10, height=5)
button_2.grid(column=1,row=0)

tick_label = Label(text="✔", font=(50))
tick_label.grid(column=0, row=0)
tick_label.config(fg=GREEN, bg=DARK)




window.mainloop()
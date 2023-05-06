import math
from tkinter import *

# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
repetitions = 0
timer = None


# ---------------------------- TIMER RESET ------------------------------- #
def reset_timer():
    window.after_cancel(timer)
    canvas.itemconfig(timer_text, text="00:00")
    timer_label.config(text="Timer")
    tick_label.config(text="")
    global repetitions
    repetitions = 0


# ---------------------------- TIMER MECHANISM ------------------------------- #
def start_timer():
    global repetitions
    repetitions += 1

    works_seconds = WORK_MIN * 60
    short_break_seconds = SHORT_BREAK_MIN * 60
    long_break_seconds = LONG_BREAK_MIN * 60

    # Need to work in the following schema: (25min work - 5min break) x 4 - 20min break.
    if repetitions % 8 == 0:
        count_down(long_break_seconds)
        timer_label.config(text="BREAK", fg=RED)
    elif repetitions % 2 == 0:
        count_down(short_break_seconds)
        timer_label.config(text="BREAK", fg=PINK)
    else:
        count_down(works_seconds)
        timer_label.config(text="WORK", fg=GREEN)


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #
def count_down(count):
    count_minute = math.floor(count / 60)
    count_seconds = count % 60
    if count_seconds < 10:
        count_seconds = f"0{count_seconds}"

    canvas.itemconfig(timer_text, text=f"{count_minute}:{count_seconds}")
    if count > 0:
        global timer
        timer = window.after(1000, count_down, count - 1)
    else:
        start_timer()
        marks = ""
        work_session = math.floor(repetitions/2)
        for _ in range(work_session):
            marks += check_mark
        tick_label.config(text=marks)


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("POMODORO")
window.config(padx=100, pady=50, bg=YELLOW)

window.after(1000)

canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
tomato_img = PhotoImage(file="tomato.png")
canvas.create_image(100, 112, image=tomato_img)
timer_text = canvas.create_text(100, 130, text="00:00", fill="white", font=(FONT_NAME, 30, "bold"))
canvas.grid(row=1, column=1)

timer_label = Label(text="Timer", bg=YELLOW, fg=GREEN, font=(FONT_NAME, 35, "bold"), pady=0)
timer_label.grid(row=0, column=1)

start_button = Button(text="START", highlightthickness=0, command=start_timer)
start_button.grid(row=2, column=0)

reset_button = Button(text="RESET", highlightthickness=0, command=reset_timer)
reset_button.grid(row=2, column=2)

check_mark = "✓"
tick_label = Label(bg=YELLOW, fg=GREEN, font=(FONT_NAME, 15, "bold"))
tick_label.grid(row=3, column=1)

window.mainloop()

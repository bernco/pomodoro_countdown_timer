from tkinter import *
import math
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps = 0

# ---------------------------- TIMER RESET ------------------------------- # 

# ---------------------------- TIMER MECHANISM ------------------------------- # 


def timer():
    global reps
    work_sec = WORK_MIN*60
    short_break_sec = SHORT_BREAK_MIN*60
    long_break_min = LONG_BREAK_MIN*60
    reps += 1
    if reps % 8 == 0:
        count_down(long_break_min)
        timer_label.config(text="Long Break", fg=RED)
    elif reps % 2 == 0:
        count_down(short_break_sec)
        timer_label.config(text="Short Break", fg=PINK)
    else:
        count_down(work_sec)
        timer_label.config(text="Work", fg=GREEN)


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 


def count_down(time_needed):
    count_min = math.floor(time_needed/60)
    count_sec = time_needed % 60
    if count_sec < 10:
        count_sec = f"0{count_sec}"
    canvas.itemconfig(canvas_text, text=f"{count_min}:{count_sec}")
    if time_needed > 0:
        window.after(1000, count_down, time_needed-1)
    else:
        timer()


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Pomorodo")
window.config(padx=100, pady=50, bg=YELLOW)

timer_label = Label(bg=YELLOW)
timer_label.config(font=(FONT_NAME, 50, "bold"), fg=GREEN)
timer_label.grid(column=2, row=1)

canvas = Canvas(bg=YELLOW, width=200, height=224, highlightthickness=0)
image = PhotoImage(file="tomato.png")
canvas.create_image(100, 112, image=image)
canvas_text = canvas.create_text(100, 130, text="00:00", font=(FONT_NAME, 34, "bold"), fill="white")

canvas.grid(column=2, row=2)

start_button = Button(text="Start", font=(FONT_NAME, 10, "bold"), highlightthickness=0, command=timer)
start_button.config(padx=3, pady=3)
start_button.grid(column=1, row=3)

check_label = Label(text="✔", fg=GREEN, bg=YELLOW, font=(FONT_NAME, 10, "bold"))
check_label.config(padx=5, pady=5)
check_label.grid(column=2, row=4)


reset_button = Button(text="Reset", font=(FONT_NAME, 10, "bold"), highlightthickness=0)
reset_button.config(padx=3, pady=3)
reset_button.grid(column=3, row=3)

window.mainloop()

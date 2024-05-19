from tkinter import *
import pygame

# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#1A5D1A"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps = 0
timer = ""

pygame.mixer.init()


def play_sound():
    pygame.mixer.music.load("bells.wav")
    pygame.mixer.music.play(loops=0)


def play_end_sound():
    pygame.mixer.music.load("urgent-tone.wav")
    pygame.mixer.music.play(loops=0)


def break_end_sound():
    pygame.mixer.music.load("break-end-bell.wav")
    pygame.mixer.music.play(loops=0)


# ---------------------------- TIMER RESET ------------------------------- #
def timer_reset():
    window.after_cancel(timer)
    canvas.itemconfig(timer_text, text="00:00")
    timer_label.config(text="Timer")
    check_mark.config(text="")
    global reps
    reps = 0


# ---------------------------- TIMER MECHANISM ------------------------------- #
def start_timer():
    global reps
    reps += 1
    if reps % 2 == 1:
        work_sec = WORK_MIN * 60
        count_down(work_sec)
        timer_label.config(text="Work", fg=GREEN)
    elif reps % 8 == 0:
        long_break = LONG_BREAK_MIN * 60
        count_down(long_break)
        timer_label.config(text="Break", fg=RED)
    elif reps % 2 == 0:
        short_break = SHORT_BREAK_MIN * 60
        count_down(short_break)
        timer_label.config(text="Break", fg=PINK)


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #
def count_down(count):
    count_seconds = count % 60
    if len(str(count_seconds)) == 1:
        count_seconds = f"0{count_seconds}"
    canvas.itemconfig(timer_text, text=f"{count // 60}:{count_seconds}")
    if count > 0:
        global timer
        timer = window.after(1000, count_down, count - 1)
    else:
        mark = ""
        for _ in range((reps + 1) // 2):
            mark += "✔"
        if reps % 2 == 1:
            if len(mark) == 4:
                play_end_sound()
            else:
                play_sound()
        check_mark.config(text=mark, fg="green")
        if reps % 2 == 0:
            break_end_sound()
        start_timer()


# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Pomodoro")
window.config(padx=100, pady=60, bg=YELLOW)

timer_label = Label(text="Timer", fg=GREEN, font=(FONT_NAME, 40, "bold"), bg=YELLOW)
timer_label.grid(column=1, row=0)

canvas = Canvas(width=200, height=225, bg=YELLOW, highlightthickness=0)
tomato_img = PhotoImage(file="tomato.png")
canvas.create_image(100, 112, image=tomato_img)
timer_text = canvas.create_text(108, 132, text="00:00", fill="white", font=(FONT_NAME, 32, "bold"))
canvas.grid(column=1, row=1)

start_button = Button(text="Start", bg="white", font=(FONT_NAME, 15, "bold"), command=start_timer)
start_button.grid(column=0, row=2)

reset_button = Button(text="Reset", bg="white", font=(FONT_NAME, 15, "bold"), command=timer_reset)
reset_button.grid(column=2, row=2)

check_mark_symbol = "✔"
check_mark = Label(fg="green", bg=YELLOW, font=(FONT_NAME, 15, "bold"))
check_mark.grid(column=1, row=3)

window.mainloop()

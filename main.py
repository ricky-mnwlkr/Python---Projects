from tkinter import *
import math

# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 1
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps = 0
timer = None
# ---------------------------- TIMER RESET ------------------------------- # 
def reset_timer():
    start_button.config(command=start_timer)
    window.after_cancel(timer)
    canvas.itemconfig(timer_text, text='00:00')
    title_label.config(text='Timer', fg=GREEN)
    check_marks.config(text='')
    global reps
    reps = 0
    
# ---------------------------- TIMER MECHANISM ------------------------------- # 

def start_timer():
    start_button.config(command='')
    global reps
    reps += 1

    work_sec = WORK_MIN * 60
    short_break_sec = SHORT_BREAK_MIN * 60
    long_break_sec = SHORT_BREAK_MIN * 60

    if reps % 8 == 0:
        title_label.config(text='Break', fg=RED)
        count_down(long_break_sec)
    elif reps % 2 == 0:
        title_label.config(text='Break', fg=PINK)
        count_down(short_break_sec)
    else:
        title_label.config(text='Work', fg=GREEN)
        count_down(work_sec)

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 
def count_down(count):
    count_min = math.floor(count / 60)
    count_sec= count % 60
    if count_sec < 10:
        count_sec = f'0{count_sec}'

    canvas.itemconfig(timer_text, text=f'{count_min}:{count_sec}')
    if count > 0:
        global timer
        timer = window.after(10, count_down, count - 1)
    else:
        start_timer()
        marks = ''
        
        
        work_session = math.floor(reps/2)
        for _ in range(work_session):
            marks += '✔'
            check_marks.config(text=marks)
            
        

# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title('Pomodoro')
window.config(padx=100, pady=50, bg=YELLOW)

tomato_img = PhotoImage(file='./tomato.png')

canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
canvas.create_image(100, 112, image=tomato_img)
timer_text = canvas.create_text(100, 130, text='00:00', fill='white', font=(FONT_NAME, 35, 'bold'))
title_label = Label(text='Timer', fg=GREEN, bg=YELLOW, font=(FONT_NAME, 50, 'bold'))

start_button = Button(text='Start', highlightthickness=0, command=start_timer)
reset_button = Button(text='Reset', highlightthickness=0, command=reset_timer)

check_marks = Label(fg=GREEN, bg=YELLOW, font=(FONT_NAME, 15))

canvas.grid(row=1, column=1)
title_label.grid(row=0, column=1)
start_button.grid(row=2, column=0)
reset_button.grid(row=2, column=2)
check_marks.grid(row=3, column=1)

window.mainloop()

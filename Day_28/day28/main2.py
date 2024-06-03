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

CHECKMARK = "✔"

reps = 0
timer = None


# ---------------------------- TIMER RESET ------------------------------- #
def reset_timer():
    window.after_cancel(timer)
    global reps
    reps = 0
    canvas.itemconfig(timer_text, text='00:00')
    lbl_timer.config( text='Timer')
    check_marks.config(text='')

# ---------------------------- TIMER MECHANISM ------------------------------- #
def start_timer():
    global reps
    reps += 1
    print(reps)
    if reps % 2 == 1:
        count_down(60 * WORK_MIN)
        lbl_timer.config(text="Work", fg=GREEN)
    elif reps % 2 == 0:
        if reps % 8 == 0:
            count_down(60 * LONG_BREAK_MIN)
            lbl_timer.config(text="Break", fg=RED)
        else:
            count_down(60 * SHORT_BREAK_MIN)
            lbl_timer.config(text="Break", fg=PINK)

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #
def count_down(count):
    global reps

    # count is in seconds
    if count >= 0:
        mins = count // 60
        secs = count % 60

        _mins = str(mins) if mins > 9 else f"0{mins}"
        _secs = str(secs) if secs > 9 else f"0{secs}"

        new_timer_text = _mins+":"+_secs
        canvas.itemconfig(timer_text, text=new_timer_text)

    if count > 0:
        global timer
        timer = window.after(1000, count_down, count - 1)
    else:
        start_timer()
        marks = ""
        for _ in range(reps // 2):
            marks += CHECKMARK
        check_marks.config(text=marks, fg=GREEN)


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Pomodoro")
window.config(padx=100, pady=50, bg=YELLOW)
window.resizable = False

lbl_timer = Label(text="Timer", font=(FONT_NAME, 50, 'normal'), bg=YELLOW, fg=GREEN)
lbl_timer.grid(column=2, row=1)

canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
tomato_img = PhotoImage(file='tomato.png')
canvas.create_image(100, 112, image=tomato_img)
timer_text = canvas.create_text(100, 130, text="00:00", font=(FONT_NAME, 35, 'bold'))
canvas.grid(column=2, row=2)

btn_start = Button(text="Start", highlightthickness=0, command=start_timer)
btn_start.grid(column=1, row=3)
btn_reset = Button(text="Reset", highlightthickness=0, command=reset_timer)
btn_reset.grid(column=3, row=3)

check_marks = Label(bg=YELLOW, fg=GREEN)
check_marks.grid(column=2, row=4)

window.mainloop()

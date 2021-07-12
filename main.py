import tkinter
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
timer = None


window = tkinter.Tk()
window.minsize(width=500,height=500)
window.config(bg=YELLOW,padx=100,pady=100)

canvas = tkinter.Canvas(window,width=220,height=224,bg=YELLOW,highlightthickness=0)

label = tkinter.Label(text="Timer",font=("Arial",25,"bold"),fg=GREEN,bg=YELLOW)
label.grid(row=0,column=1)
img = tkinter.PhotoImage(file="tomato.png")
canvas.create_image(110, 112, image=img)
timer_text = canvas.create_text(110,132,text="00:00",fill="white",font=(FONT_NAME,20,"bold"))
canvas.grid(row=1,column=1)

def update_count(count):
    minutes = math.floor(count/60)
    seconds = count%60
    if seconds < 10:
        seconds = f"0{seconds}"
    if count >= 0:
        global timer
        canvas.itemconfig(timer_text,text=f"{minutes}:{seconds}")
        timer = window.after(1000, update_count, count-1)
    else:
        start_countdown()
        check_mark = ""
        for _ in range(math.floor(float(reps)/2)):
            check_mark = check_mark + "✓"
        check_marks.config(text=check_mark)

def reset_countdown():
    global reps
    reps = 0
    window.after_cancel(timer)
    check_marks.config(text="")
    label.config(text="TImer")
    canvas.itemconfig(timer_text,text="00:00")

def start_countdown():
    global reps
    reps = reps + 1
    print(reps)
    if reps % 2 == 0:
        if reps % 8 ==0:
            label.config(text="Break",fg=PINK)
            update_count(20*60)
        else:
            label.config(text="Break", fg=PINK)
            update_count(5*60)
    else:
        label.config(text="Work", fg=GREEN)
        update_count(25*60)

start_button=tkinter.Button(text="start",command = start_countdown)
start_button.grid(row=2,column=0)


reset_button=tkinter.Button(text="start",command=reset_countdown)
reset_button.grid(row=2,column=2)

check_marks = tkinter.Label(font=("Arial", 15, "bold"), bg=YELLOW, fg=GREEN)
check_marks.grid(row=3, column=1)

window.mainloop()
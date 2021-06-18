from tkinter import *
import tkinter.scrolledtext as scrolledtext

count = 0
clock = None
time= 9

def start_timer(t):
    global count
    if count >= 1 :
        if t >= 0:
            text.config(foreground='red')
            timer.config(text=f"Time: {t} sec")
            global clock
            clock = window.after(1000, start_timer, t - 1) #window after 1000ms, t-1 (timer in second)
            if t == 3:
                text.config(foreground='#E2E2E2')
            if t == 2:
                text.config(foreground='#F0F0F0')
            if t == 1:
                text.config(foreground='#FFFFFF')
            if t == 0:
                text.config(state="disable", foreground='green')
                #text need unbind for keep value count == 0 (not starting the timer)
                text.unbind('<Key>')

def key_press(event):
    global count, time, clock
    if count == 0 :
        count += 1
        start_timer(time)
    else : #count==1. when typing count == 1, time back into 9
        window.after_cancel(clock) #stop/cancel variable clock
        time = 9
        start_timer(time)

        # #for testing
        # print(count)


window = Tk()
window.title("Dangerous Writing Apps")
window.config(padx=100, pady=100, bg="#FAF1E6")
window.geometry("1440x1000")

title = Label(text="---Dangerous Writing Apps---", font="Times 40", bg="#FAF1E6")
title.grid(row=0, column=0)

#tkinter typing area
text = scrolledtext.ScrolledText(font="Times 22", bg="#FDFAF6", height=20, padx=20, pady=3, foreground='red')
text.grid(row=1, column=0, padx=20, pady=20)

timer = Label(text=f"Time: {time} sec", font="Times 30", bg="#FAF1E6")
timer.grid(row=4, column=0)

#binding function, for detect when user typing / not
text.bind('<Key>', key_press)

window.mainloop()
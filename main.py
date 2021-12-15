import time
import tkinter as tk
from threading import *

def change_label():
    while True:
        a = time.localtime()
        timevar = str(a.tm_year) + "/" + str(a.tm_mon) + "/" + str(a.tm_mday) + "\n" + str(a.tm_hour) + ":" + str(a.tm_min) + ":" + str(a.tm_sec)
        label3 = tk.Label(text=timevar, fg="green", font=('Arial', 20),bg='#202121')
        label3.place(x=180,y=100)
        time.sleep(1)
        label3.destroy()

window = tk.Tk()
window.geometry("500x400")
window.title("Clock")
window.config(background='#202121')
canvas = tk.Canvas(window, width = 300, height = 300,bg='#202121',borderwidth=0,highlightthickness=0)

img = tk.PhotoImage(file='clock.png')
canvas.create_image(200,200,anchor=tk.NE, image=img)
canvas.pack()
display_time = Thread(target=change_label, daemon = True)
display_time.start()
window.mainloop()

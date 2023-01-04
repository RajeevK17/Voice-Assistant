import sys
from tkinter import *
from PIL import ImageTk, Image

try:
    import sara
except:
    print("Please check your internet connection!")
    sys.exit()

win = Tk()
win.title('Sara')
win.minsize(625, 700)
win.maxsize(625, 700)

frame = Frame(win, width=625, height=700)
frame.place(x=0, y=0)

start_button = Button(win, text='Start!', fg = 'black', bg = '#39FF14', command=sara.run, border=0)
start_button.place(x=290, y=650)

img = ImageTk.PhotoImage(Image.open("sara.png"))

label = Label(frame, image = img)
label.place(x=-1, y=-1)
win.mainloop()
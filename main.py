from tkinter import *
from tkinter import filedialog
from turtle import title

screen = Tk()
title = screen.title('youtube download')
canvas = Canvas(screen, width=500, height=500)
canvas.pack()


logo = PhotoImage(file="yt.png")

logo= logo.subsample(2,2)

canvas.create_image(250,80,image=logo)
screen.mainloop()
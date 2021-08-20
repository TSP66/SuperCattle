from tkinter import Tk, Canvas,SW
from random import choice

colours = ['red','green','yellow']

width = 1600
height = 900

size = 50

master = Tk()

master.title("SuperCattle")

window = Canvas(master, width=width, height=height)

for x in range(int(width/size)-1):
    for y in range(int(height/size)-1):
        colour = choice(colours)
        window.create_rectangle(x*size, y*size, (x+1)*size, (y+1)*size, fill=colour, outline = colour)

window.create_text(450,325,fill='black',font="Arial 30 italic bold",text="• Current Location")
window.create_text(800,725,fill='black',font="Arial 30 italic bold",text="• Dam")
window.create_text(550,525,fill='black',font="Arial 30 italic bold",text="• Dam")
window.create_text(775,225,fill='black',font="Arial 30 italic bold",text="• Station")

window.pack()

master.mainloop() 

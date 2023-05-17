from tkinter import *

def entrance_image():
  root = Tk()
  canvas = Canvas(root, width = 788, height = 362)
  canvas.pack()
  img = PhotoImage(file="images/97e48b8f1871c760fde186411970378e (1).png")      
  canvas.create_image(20,20, anchor=NW, image=img)      
  mainloop()
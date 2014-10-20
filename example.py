##########################################
#                                        #
#    Example of drawing with Canvas      #
#                                        #
##########################################

from Tkinter import *
root = Tk()
# Create the canvas widget
drawpad = Canvas(root, width=800,height=600, background='grey')
drawpad.grid(row=0, column=1)
# Overlapped the Rectangle roof for the Chimney
square = drawpad.create_rectangle(400,150,450,300, fill='blue')
oval = drawpad.create_oval(100,400,500,200, fill='red')
#Just started making a Bootyful House
square = drawpad.create_rectangle(100,300,500,500, fill='red')
square = drawpad.create_rectangle(400,400,450,500, fill='blue')
square = drawpad.create_rectangle(110,400,160,450, fill='pink')
square = drawpad.create_rectangle(180,400,230,450, fill='pink')
square = drawpad.create_rectangle(240,400,290,450, fill='pink')
square = drawpad.create_rectangle(310,400,360,450, fill='pink')
square = drawpad.create_rectangle(0,500,800,600, fill='green')
# Just made a kickass line
line = drawpad.create_line(0, 0, 200, 100)
root.mainloop()
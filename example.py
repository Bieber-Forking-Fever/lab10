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
# create_oval(x,y,width,height,fill color)
oval = drawpad.create_oval(100,400,500,200, fill='red')
#create_square(top left x,top left y, bottom right x, bottom right y, fill color)
square = drawpad.create_rectangle(100,300,500,500, fill='red')
square = drawpad.create_rectangle(400,400,450,500, fill='blue')
square = drawpad.create_rectangle(400,300,450,500, fill='blue')
square = drawpad.create_rectangle(350,400,390,450, fill='pink')
square = drawpad.create_rectangle(300,400,350,450, fill='pink')
square = drawpad.create_rectangle(250,400,310,450, fill='pink')
square = drawpad.create_rectangle(200,400,270,450, fill='pink')
square = drawpad.create_rectangle(0,500,800,600, fill='green')
#create_line(top left x,top left y, bottom right x, bottom right y, fill color)
line = drawpad.create_line(0, 0, 200, 100)
root.mainloop()
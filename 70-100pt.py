
##########################################
#                                        #
#             Draw a house!              #
#                                        #
##########################################

# Use create_line(), create_rectangle() and create_oval() to make a 
# drawing of a house using the tKinter Canvas widget.

# 70pt: House outline (roof and the house)
# 80pt: Square windows and a door
# 90pt: A door handle plus a chimney!
# 100pt: Green grass on the ground and a red house!

# Minus 5pts if your code has no comments
# Minus 10pts if you only commit once to github.

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
# Just made a kickass Doorknob and Door
line = drawpad.create_line(0, 0, 200, 100)
oval = drawpad.create_oval(435,445,450,460, fill='red')
root.mainloop()






            




















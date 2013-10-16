import _tkinter
import Tkinter
from Tkinter import *

import turtle

def sierpinski(length,depth):
    if depth>1:turtle.dot()
    if depth==0:
        turtle.stamp()
    else:
        turtle.forward(length)
        sierpinski(length/2,depth-1)
        turtle.backward(length)
        turtle.left(120)
        turtle.forward(length)
        sierpinski(length/2,depth-1)
        turtle.backward(length)
        turtle.left(120)
        turtle.forward(length)
        sierpinski(length/2,depth-1)
        turtle.backward(length)
        turtle.left(120)

    # mainloop()
sierpinski(200,6)


from tkinter import *
from Ball import *
import time

window = Tk()

WIDTH = 500
HEIGHT = 500

canvas = Canvas(window,width=WIDTH,height=HEIGHT)
canvas.pack()

volley_ball = Ball(canvas,0,0,100,1,1,"orange")
xx_ball = Ball(canvas,0,0,50,3,1,"blue")
xy_ball = Ball(canvas,0,0,70,8,4,"green")
yy_ball = Ball(canvas,0,0,10,2,3,"purple")
yx_ball = Ball(canvas,0,0,30,2,5,"black")

while True:
    volley_ball.move()
    xx_ball.move()
    xy_ball.move()
    yy_ball.move()
    yx_ball.move()
    window.update()
    time.sleep(0.01)

window.mainloop()
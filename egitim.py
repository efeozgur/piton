from turtle import *
from os import * 


t = Turtle()
a=0
t.speed(10)
t.pensize(4)

def koordinat(x,y):
    print("x : ", x, "y: ", y)


ekran = t.getscreen()
t.up()
ekran.onclick(t.get_poly())
t.down()

mainloop()
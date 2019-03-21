import turtle
import math
from typing import List

t=turtle.Turtle()
t.getscreen().bgcolor("#771849")
colors= [ '#f269d3', '#d9f549','#d10e37', 'black', '#a295a7','#50a9e7']
t.pensize(1)
t.speed(20)
for x in range(360):
    t.pencolor(colors[x%6])
    t.width(x/100+1)
    t.forward(x)
    t.left(59)


turtle.done()


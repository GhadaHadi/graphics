import turtle
t=turtle.Turtle()
t.speed(100)
t.getscreen().bgcolor("#771849")
colors = ["red", "yellow", "blue", "green"]
for x in range(100):
    t.pencolor(colors[x % 4])
    t.forward(x+5)
    t.left(90)





turtle.done()
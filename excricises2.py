import turtle
t=turtle.Turtle()
t.speed(10)
def cycle1(x,y,pen):
 t.hideturtle()
 turtle.bgcolor("gray")

 t.left(x)
 t.forward(y)

 t.right(90)

 t.color(pen)
 t.circle(66)
 t.pencolor("black")
 t.home()

t.begin_fill()
cycle1(120,70,"#771849")
t.end_fill()
t.begin_fill()
cycle1(70,70,"#f2ce3e")
t.end_fill()
t.begin_fill()
cycle1(80,200,"#e96883")
t.end_fill()
t.begin_fill()
cycle1(105,288,"darkorange")
t.end_fill()

turtle.done()
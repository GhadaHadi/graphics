import turtle
c=turtle.Turtle()
c.getscreen().bgcolor("#907047")
c.pensize(5)
c.speed(10)

#circle1
c.up()
c.goto(0,-200)
c.down()
c.pencolor("black")
c.fillcolor("#b2777b")
c.begin_fill()
c.circle(200)
c.end_fill()
#circle2
c.up()
c.goto(0,-150)
c.down()
c.pencolor("black")
c.fillcolor("#e3b947")
c.begin_fill()
c.circle(150)
c.end_fill()

#circle3
c.up()
c.goto(0,-100)
c.down()
c.pencolor("black")
c.fillcolor("#e3b9c1")
c.begin_fill()
c.circle(100)
c.end_fill()

#circle4
c.up()
c.goto(0,-50)
c.down()
c.pencolor("black")
c.fillcolor("#82b9c1")
c.begin_fill()
c.circle(50)
c.end_fill()


turtle.done()


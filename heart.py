import turtle
heart=turtle.Turtle()
heart.speed(0)
heart.getscreen().bgcolor("black")
heart.pensize(2)

def love():
    for i in range(200):
        heart.right(1)
        heart.forward(1)
heart.speed(30)
heart.color("#bb1e11")
heart.begin_fill()
heart.left(140)
heart.forward(111.65)
love()
heart.left(120)
love()
heart.forward(111.65)
heart.end_fill()
heart.hideturtle()
turtle.done()



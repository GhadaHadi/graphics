import turtle
t=turtle.Turtle()
t.pencolor("red")
t.getscreen().bgcolor("black")

def trangle(length,depth):
    if depth==0:
        t.forward(length)
        t.left(120)
    else:
        trangle(length/2,depth-1)
        t.forward(length/2)
        trangle(length/2,depth-1)
        t.back(length/2)
        t.left(60)
        t.forward(length/2)
        t.right(60)
        trangle(length/2,depth-1)
        t.left(60)
        t.back(length/2)
        t.right(60)

t.speed(20)
trangle(500,6)
t.ht()
turtle.done()
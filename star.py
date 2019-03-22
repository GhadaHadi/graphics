import  turtle
s=turtle.Turtle()
s.speed(30)
s.getscreen().bgcolor("black")
#colors=['yellow','red','green','blue','orange']
s.penup()
s.goto((-200,100))
s.pendown()

def star(turtle,size):
    if size <=10:
        return
    else:
        turtle.begin_fill()
        for i in range(5):
           s.pencolor("#b2777b")
           turtle.forward(size)
           star(turtle,size/3)
           turtle.left(216)
        turtle.end_fill()

star(s,360)

turtle.done()

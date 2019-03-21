import turtle
m=turtle.Turtle()
m.shape("blank")
m.penup()
for i in range(30,-1,-1):
    m.color("red")
    m.stamp()
    m.dot(20)
    m.right(i)
    m.forward(20)

turtle.done()
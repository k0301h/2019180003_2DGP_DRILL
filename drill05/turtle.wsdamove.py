import turtle

def upmove_turtle():
    turtle.stamp()
    turtle.setheading(90)
    turtle.forward(50)

def rightmove_turtle():
    turtle.stamp()
    turtle.setheading(0)
    turtle.forward(50)

def downmove_turtle():
    turtle.stamp()
    turtle.setheading(270)
    turtle.forward(50)

def leftmove_turtle():
    turtle.stamp()
    turtle.setheading(180)
    turtle.forward(50)

def restart():
    turtle.reset()

turtle.shape('turtle')

turtle.onkey(upmove_turtle, 'w')
turtle.onkey(rightmove_turtle, 'd')
turtle.onkey(downmove_turtle, 's')
turtle.onkey(leftmove_turtle, 'a')
turtle.onkey(restart, 'Escape')
turtle.listen()

import turtle
import random

def reset():
    turtle.reset()

def drunken_move():
    turtle.setheading(random.randint(0,360))
    turtle.forward(random.randint(50,300))
    turtle.stamp()

turtle.shape("turtle")
turtle.onkey(drunken_move, ' ')
turtle.onkey(reset, 'Escape')
turtle.listen()

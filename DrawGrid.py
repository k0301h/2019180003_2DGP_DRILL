import turtle

index = 0
while(index < 6):
    turtle.pendown()
    turtle.forward(250)
    turtle.penup()
    index += 1
    turtle.goto(0,index * 50)

index = 0
turtle.goto(0,0)
turtle.setheading(90)

while(index < 6):
    turtle.pendown()
    turtle.forward(250)
    turtle.penup()
    index += 1
    turtle.goto(index * 50,0)

index = 0
turtle.goto(0,0)
turtle.setheading(0)

turtle.exitonclick()

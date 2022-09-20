import turtle

turtle.reset()

# testlead time - 어떤 부분코드를 실행하기위해 앞의 코드를 실행하는데 걸리는 시간
# ==> 가장 마지막에 있는 스테이지의 문스터를 수정 ==> 마지막 스테이지를 갈려는 시간
# 스테이지 별로 따로 플레이 할수있게 제작을 한다
# draw horizonal lines - 가로줄 그리기

y = -100
while y <= 400:
    turtle.penup()
    turtle.goto(-100, y)
    turtle.pendown()
    turtle.goto(400, y)
    y += 100


# draw vertical lines - 가로줄 그리기

x = - 100
while x <= 400:
    turtle.penup()
    turtle.goto(x, -100)
    turtle.pendown()
    turtle.goto(x, 400)
    x += 100

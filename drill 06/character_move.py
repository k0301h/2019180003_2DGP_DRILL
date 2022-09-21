from pico2d import *
import math

open_canvas()

# fill here
grass = load_image('grass.png')
character = load_image('character.png')

x = 400
y = 90
radian = 0
while 1 :
    while(x < 780): # 오른쪽 이동
        clear_canvas_now()
        grass.draw_now(400, 30)
        character.draw_now(x, y)
        x = x + 2
        delay(0.01)
    while(y < 560): # 위로 이동
        clear_canvas_now()
        grass.draw_now(400, 30)
        character.draw_now(x, y)
        y = y + 2
        delay(0.01)
    while(x > 20): # 왼쪽으로 이동
        clear_canvas_now()
        grass.draw_now(400, 30)
        character.draw_now(x, y)
        x = x - 2
        delay(0.01)
    while(y > 90): # 아래로 이동
        clear_canvas_now()
        grass.draw_now(400, 30)
        character.draw_now(x, y)
        y = y - 2
        delay(0.01)
    while(x < 400): # 시작지점(400,90)으로 이동
        clear_canvas_now()
        grass.draw_now(400, 30)
        character.draw_now(x, y)
        x = x + 2
        delay(0.01)
    while(radian < 720): # 원형 이동
        clear_canvas_now()
        grass.draw_now(400, 30)
        character.draw_now(x, y)
        radian = radian + 2;
        x = x - 3.5 * math.cos(radian / 360 * math.pi)
        y = y + 3.5 * math.sin(radian / 360 * math.pi)
        delay(0.01)
    radian = 0
    
close_canvas()

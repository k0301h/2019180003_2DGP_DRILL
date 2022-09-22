from pico2d import *
import math

open_canvas()

space = load_image('space.png')
sun = load_image('sun.png')
earth = load_image('earth.png')
moon = load_image('moon.png')
penguin = load_image('penguin.png')

earthframe = 0
moonframe = 0
penguinframe = 0

def draw_all(ex, ey, mx, my, earthframe, moonframe, px, penguinframe):
        clear_canvas()
    # 적절한 해 스프라이트를 찾지못해 일반 png로 대채하였습니다.
        space.draw(400, 300)
        sun.draw(400, 300)
    # 달 스프라이트의 시작 위치를 (0, 80)으로 설정함 (우하향), 지구도 같은이유로(0, 167)으로 설정
        moon.clip_draw(moonframe % 4 * 20, 80 - moonframe // 4 * 20, 20, 20, mx, my) 
        earth.clip_draw(earthframe % 5 * 33, 167 - earthframe // 5 * 33, 33, 33, ex, ey)
        penguin.clip_draw(penguinframe % 9 * 62, 940 -  penguinframe // 9 * 62, 62, 62, px + 300, 62)
        update_canvas()
        delay(0.1)

def earth_circle_calculation(cx,cy,r,deg):
    x = cx + r * math.cos(deg / 360 * 2 * math.pi)
    y = cy + r * math.sin(deg / 360 * 2 * math.pi)
    return x,y

# 공전속도는 달이 더 빠르게 제작 
def moon_circle_calculation(cx,cy,r,deg):
    x = cx + r * math.cos(deg / 180 * 2 * math.pi)
    y = cy + r * math.sin(deg / 180 * 2 * math.pi)
    return x,y

def orbit_move(earthframe, moonframe,penguinframe):
    ecx , ecy, er = 400, 300 ,150
    for deg in range(-90, 270, 5):
        ex,ey = earth_circle_calculation(ecx,ecy,er,deg)

        mcx , mcy, mr = ex, ey, 50
        mx,my = moon_circle_calculation(mcx,mcy,mr,deg)

        draw_all(ex,ey,mx,my,earthframe, moonframe, deg, penguinframe)

        moonframe = (moonframe + 1) % 19
        earthframe = (earthframe + 1) % 30
        penguinframe = (penguinframe + 1) % 27


while(1):
    orbit_move(earthframe, moonframe,penguinframe)
    get_events()

close_canvas()

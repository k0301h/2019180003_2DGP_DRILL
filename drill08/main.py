from pico2d import *

def handle_events():
    global running
    global xdir
    global ydir
    global motion
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            running = False
        elif event.type == SDL_KEYDOWN:
            if event.key == SDLK_RIGHT:
                xdir += 1
                motion = 2
            elif event.key == SDLK_LEFT:
                xdir -= 1
                motion = 3
            elif event.key == SDLK_UP:
                ydir += 1
                if motion == 0:
                    motion = 2
                elif motion == 1:
                    motion = 3
            elif event.key == SDLK_DOWN:
                ydir -= 1
                if motion == 0:
                    motion = 2
                elif motion == 1:
                    motion = 3
            elif event.key == SDLK_ESCAPE:
                running = False
        elif event.type == SDL_KEYUP:
            if event.key == SDLK_RIGHT:
                xdir -= 1
                motion = 0
            elif event.key == SDLK_LEFT:
                xdir += 1
                motion = 1
            elif event.key == SDLK_UP:
                ydir -= 1
                if motion == 2:
                    motion = 0
                elif motion == 3:
                    motion = 1
            elif event.key == SDLK_DOWN:
                ydir += 1
                if motion == 2:
                    motion = 0
                elif motion == 3:
                    motion = 1

open_canvas()
kpu_ground = load_image('TUK_GROUND.png')
character = load_image('animation_sheet.png')
KPU_WIDTH, KPU_HEIGHT = 800, 600

running = True
motion = 0
x, y = KPU_WIDTH // 2, KPU_HEIGHT // 2
frame = 0
xdir = 0
ydir = 0
hide_cursor()

while running:
    clear_canvas()
    kpu_ground.draw(KPU_WIDTH // 2, KPU_HEIGHT // 2)
    if motion == 0:
        character.clip_draw(frame * 100, 300, 100, 100, x, y)
    elif motion == 1:
        character.clip_draw(frame * 100, 200, 100, 100, x, y)
    elif motion == 2:
        character.clip_draw(frame * 100, 100 * 1, 100, 100, x, y)    
    elif motion == 3:
        character.clip_draw(frame * 100, 0, 100, 100, x, y)
        
    update_canvas()

    handle_events()
    frame = (frame + 1) % 8

    x += xdir * 5
    y += ydir * 5

#다른 알고리즘이 생각이 안나서 이렇게 짰습니다.
    if 0 > x:
        x = 0
    elif x > KPU_WIDTH:
        x = KPU_WIDTH
    elif y < 0:
        y = 0
    elif y > KPU_HEIGHT:
        y = KPU_HEIGHT
        
    delay(0.01)

close_canvas()


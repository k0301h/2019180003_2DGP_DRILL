from boy_grass_object import *
import game_framework
import delete_state

boy = None
grass = None
running = None
# 초기화
def enter():
    global boy, grass, running
    boy = Boy()
    grass = Grass()
    running = True
# 종료
def exit():
    global boy, grass
    del boy
    del grass

def update():
    boy.update()

def draw_world():
    grass.draw()
    boy.draw()

def draw():
    clear_canvas()
    draw_world()
    update_canvas()

def handle_events():
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            game_framework.quit()
        elif event.type == SDL_KEYDOWN:
            if event.key == SDLK_b:
                game_framework.push_state(delete_state)
            elif event.key == SDLK_ESCAPE:
                game_framework.quit()

def pause(): pass

def resume(): pass

def test_self():
    import sys
    pico2d.open_canvas()
    game_framework.run(sys.modules['__main__'])
    pico2d.clear_canvas()

if __name__ == '__main__':
    test_self()

class Boy:
    def __init__(self):
        self.x, self.y = 0, 90
        self.frame = 0
        self.dir, self.face_dir = 0, 1
        self.image = load_image('animation_sheet.png')
        self.item = None

    def update(self):
        self.frame = (self.frame + 1) % 8
        self.x += self.dir * 1
        self.x = clamp(0, self.x, 800)


    def draw(self):
        if self.dir == -1:
            self.image.clip_draw(self.frame*100, 0, 100, 100, self.x, self.y)
        elif self.dir == 1:
            self.image.clip_draw(self.frame*100, 100, 100, 100, self.x, self.y)
        else:
            if self.face_dir == 1:
                self.image.clip_draw(self.frame * 100, 300, 100, 100, self.x, self.y)
            else:
                self.image.clip_draw(self.frame * 100, 200, 100, 100, self.x, self.y)

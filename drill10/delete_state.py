from pico2d import *
import game_framework
import play_state

image = None

def handle_events():
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            game_framework.quit()
        elif event.type == SDL_KEYDOWN:
            if event.key == SDLK_ESCAPE:
                game_framework.pop_state()
            elif event.key == SDLK_PLUS:
                play_state.boy
            elif event.key == SDLK_MINUS:
                pass

def enter():
    global image
    image = load_image('add_delete_boy.png')

def draw():
    clear_canvas()
    play_state.draw_world()
    image.draw(400,300)
    update_canvas()

def exit():
    global image
    del image

def update(): pass

def pause(): pass
def resume(): pass

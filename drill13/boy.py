from pico2d import *
import game_world
from ball import Ball
import game_framework
import random

#1 : 이벤트 정의
RD, LD, RU, LU, TIMER = range(5)
event_name = ['RD', 'LD', 'RU', 'LU', 'TIMER', 'SPACE']

key_event_table = {
    (SDL_KEYDOWN, SDLK_RIGHT): RD,
    (SDL_KEYDOWN, SDLK_LEFT): LD,
    (SDL_KEYUP, SDLK_RIGHT): RU,
    (SDL_KEYUP, SDLK_LEFT): LU
}


#2 : 상태의 정의
class IDLE:
    @staticmethod
    def enter(self,event):
        print('ENTER IDLE')
        self.dir = 0
        self.timer = 1000

    @staticmethod
    def exit(self, event):
        print('EXIT IDLE')

    @staticmethod
    def do(self):
        self.frame = (self.frame + FRAME_PER_ACTION * ACTION_PER_TIME * game_framework.frame_time) % 14
        self.timer -= 1
        if self.timer == 0:
            self.add_event(TIMER)


    @staticmethod
    def draw(self):
        if self.face_dir == 1:
            self.image.clip_composite_draw(int(self.frame) % 5 * 183, int(self.frame) // 5 * 168, 183, 168, 0, '', self.x, self.y, 100, 100)
        else:
            self.image.clip_composite_draw(int(self.frame) % 5 * 183, int(self.frame) // 5 * 168, 183, 168, 0, 'h',
                                           self.x, self.y, 100, 100)


class RUN:
    def enter(self, event):
        print('ENTER RUN')

    def exit(self, event):
        print('EXIT RUN')
        self.face_dir = self.dir

    def do(self):
        self.frame = (self.frame + FRAME_PER_ACTION * ACTION_PER_TIME * game_framework.frame_time) % 14
        self.x += self.dir * RUN_SPEED_PPS * game_framework.frame_time

        self.x = clamp(0, self.x, 1600)
        if self.x >= 1600:
            self.dir = -1
        elif self.x <= 0:
            self.dir = 1

    def draw(self):
        if self.dir == 1:
            self.image.clip_composite_draw(int(self.frame) % 5 * 183, int(self.frame) // 5 * 168, 183, 168, 0, '',
                                           self.x, self.y, 50, 50)
        else:
            self.image.clip_composite_draw(int(self.frame) % 5 * 183, int(self.frame) // 5 * 168, 183, 168, 0, 'h',
                                           self.x, self.y, 50, 50)


class SLEEP:

    def enter(self, event):
        print('ENTER SLEEP')
        self.frame = 0

    def exit(self, event):
        pass

    def do(self):
        self.frame = (self.frame + FRAME_PER_ACTION * ACTION_PER_TIME * game_framework.frame_time) % 14

    def draw(self):
        if self.face_dir == 1:
            self.image.clip_composite_draw(int(self.frame) % 5 * 183, int(self.frame) // 5 * 168, 183, 168, 3.141592 / 2, '',
                                           self.x, self.y, 100, 100)
        else:
            self.image.clip_composite_draw(int(self.frame) % 5 * 183, int(self.frame) // 5 * 168, 183, 168, -3.141592 / 2, 'h',
                                           self.x, self.y, 100, 100)


#3. 상태 변환 구현

next_state = {
    IDLE:  {RU: RUN,  LU: RUN,  RD: RUN,  LD: RUN, TIMER: SLEEP},
    RUN:   {RU: RUN, LU: RUN, RD: RUN, LD: RUN},
    SLEEP: {RU: RUN, LU: RUN, RD: RUN, LD: RUN}
}

TIME_PER_ACTION = 0.5
ACTION_PER_TIME = 1.0 / TIME_PER_ACTION
FRAME_PER_ACTION = 8

PIXEL_PER_METER = 10 / 0.3
RUN_SPEED_KPH = 100 # 20 km/h 마라토너
RUN_SPEED_MPM = RUN_SPEED_KPH * 1000 / 60
RUN_SPEED_MPS = RUN_SPEED_MPM / 60
RUN_SPEED_PPS = RUN_SPEED_MPS * PIXEL_PER_METER

class BIRD:
    def __init__(self):
        self.x, self.y = 500 + random.randint(-300, 300), 300 + random.randint(-100, 100)
        self.frame = 0
        self.dir, self.face_dir = 1, 1
        self.image = load_image('bird_animation.png')
        self.font = load_font('ENCR10B.TTF', 16)

        self.timer = 100

        self.event_que = []
        self.cur_state = RUN
        self.cur_state.enter(self, None)

    def update(self):
        self.cur_state.do(self)

        if self.event_que:
            event = self.event_que.pop()
            self.cur_state.exit(self, event)
            try:
                self.cur_state = next_state[self.cur_state][event]
            except KeyError:
                print(f'ERROR: State {self.cur_state.__name__}    Event {event_name[event]}')
            self.cur_state.enter(self, event)

    def draw(self):
        self.cur_state.draw(self)
        self.font.draw(self.x - 60, self.y + 50, f'(Time : {get_time():.2f})', (255, 255, 0))

    def add_event(self, event):
        self.event_que.insert(0, event)

    def handle_event(self, event):
        if (event.type, event.key) in key_event_table:
            key_event = key_event_table[(event.type, event.key)]
            self.add_event(key_event)

from pico2d import *

# event define
RD, LD, RU, LU = range(4) # ==> 0, 1, 2, 3

key_event_table = {
    (SDL_KEYDOWN, SDLK_RIGHT):RD,
    (SDL_KEYDOWN, SDLK_LEFT):LD,
    (SDL_KEYUP, SDLK_RIGHT):RU,
    (SDL_KEYUP, SDLK_LEFT):LU
}

# class를 이용해서 상태를 제작
class IDLE:
    @staticmethod
    def enter():
        print('enter idle')

    @staticmethod
    def exit():
        print('exit idle')

    @staticmethod
    def do():
        pass

    @staticmethod
    def draw():
        pass

class RUN:
    def enter():
        print('enter run')

    def exit():
        print('exit run')

    def do():
        pass

    def draw():
        pass

next_state = {
    IDLE : {RU : RUN, LU:RUN, RD:RUN, LD:RUN}, # RU, LU는 동시에 입력시 떼었을떄 움직여야 하니 RUN
    RUN : {RU : IDLE, LU:IDLE, RD:IDLE, LD:IDLE}
}



class Boy:
    def add_event(self, event):
        self.q.insert(0, event)

    def handle_event(self, event): # 소년이 스스로 이ㅔㅂㄴ트를 처리할수 있게 ㅔㅈ작
        # if event.type == SDL_KEYDOWN:
        #     match event.key:
        #         case pico2d.SDLK_LEFT:
        #             self.dir -= 1
        #         case pico2d.SDLK_RIGHT:
        #             self.dir += 1
        # elif event.type == SDL_KEYUP:
        #     match event.key:
        #         case pico2d.SDLK_LEFT:
        #             self.dir += 1
        #             self.face_dir = -1
        #         case pico2d.SDLK_RIGHT:
        #             self.dir -= 1
        #             self.face_dir = 1
        # event는 키이벤트 => 이것을 내부 RD들으로 변환
        if(event.type, event.key) in key_event_table:
            key_event = key_event_table[(event.type, event.key)]
            self.add_event(key_event) # 변환된 내부 이벤트를 큐에 추가
        if self.q: # q에 뭔가 들어있다면
            event = self.q.pop()        # event bring
            self.cur_state.exit()       # now state exit
            self.cur_state = next_state[self.cur_state][event]  # next state calculate
            self.cur_state.enter()      # next state enter



    def __init__(self):
        self.x, self.y = 0, 90
        self.frame = 0
        self.dir, self.face_dir = 0, 1
        self.image = load_image('animation_sheet.png')

        self.q = []
        self.cur_state = IDLE
        self.cur_state.enter()

    def update(self):
        # self.frame = (self.frame + 1) % 8
        # self.x += self.dir * 1
        # self.x = clamp(0, self.x, 800)
        self.cur_state.do()

    def draw(self):
        # if self.dir == -1:
        #     self.image.clip_draw(self.frame*100, 0, 100, 100, self.x, self.y)
        # elif self.dir == 1:
        #     self.image.clip_draw(self.frame*100, 100, 100, 100, self.x, self.y)
        # else:
        #     if self.face_dir == 1:
        #         self.image.clip_draw(self.frame * 100, 300, 100, 100, self.x, self.y)
        #     else:
        #         self.image.clip_draw(self.frame * 100, 200, 100, 100, self.x, self.y)
        self.cur_state.draw()

    def add_event(self,event):
        pass
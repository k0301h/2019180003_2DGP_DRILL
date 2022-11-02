from pico2d import *

# event define
RD, LD, RU, LU, TIMER, AUTO = range(6) # ==> 0, 1, 2, 3

key_event_table = {
    (SDL_KEYDOWN, SDLK_RIGHT):RD,
    (SDL_KEYDOWN, SDLK_LEFT):LD,
    (SDL_KEYUP, SDLK_RIGHT):RU,
    (SDL_KEYUP, SDLK_LEFT):LU,
    (SDL_KEYUP, SDLK_a):AUTO
}


class AUTORUN:
    def enter(self, event):
        print('enter autorun')
        self.dir = self.face_dir
        pass

    def exit(self):
        print('exit autorun')
        #run울 나가서 idle로 갈때 run의 방향을 알려줗 필요가 있다.
        self.face_dir = self.dir
        self.dir = 0
        pass

    def do(self):
        self.frame = (self.frame + 1) % 8
        self.x += self.dir
        self.x = clamp(0, self.x, 800) # 0 < self.x < 800
        if self.x == 800:
            self.dir = -1
        elif self.x == 0:
            self.dir = 1
        pass

    def draw(self):
        if self.dir == -1:
            self.image.clip_draw(self.frame*100, 0, 100, 100, self.x, self.y + 50, 200, 200)
        elif self.dir == 1:
            self.image.clip_draw(self.frame*100, 100, 100, 100, self.x, self.y + 50, 200, 200)
        pass

class SLEEP:
    @staticmethod
    def enter(self, event):
        print('enter sleep')
        self.dir = 0
        pass

    @staticmethod
    def exit(self):
        print('exit sleep')
        pass

    @staticmethod
    def do(self):
        self.frame = (self.frame + 1) % 8
        pass

    @staticmethod
    def draw(self):
        if self.face_dir == 1: # right look
            self.image.clip_composite_draw(self.frame * 100, 300, 100, 100,
                                 3.141592/2, '',
                                 self.x, self.y - 30, 100, 100)
        else:
            self.image.clip_composite_draw(self.frame * 100, 200, 100, 100,
                                           -3.141592/2, '',
                                           self.x, self.y - 30, 100, 100)
        pass

# class를 이용해서 상태를 제작
class IDLE:
    @staticmethod
    def enter(self, event):
        print('enter idle')
        self.dir = 0
        #timer set
        self.timer = 1000
        pass

    @staticmethod
    def exit(self):
        print('exit idle')
        pass

    @staticmethod
    def do(self):
        self.frame = (self.frame + 1) % 8
        self.timer -= 1
        if self.timer == 0: # 시간이 경과 하면
            # 이벤트를 발생해야 한다.
            # self.q.insert(0, TIMER) # 객체지향 프로그램 X ==> q를 직접 엑세스 하고있으니깐
            self.add_event(TIMER) # 객체지향적인 방법
        pass

    @staticmethod
    def draw(self):
        if self.face_dir == 1: # right look
            self.image.clip_draw(self.frame * 100, 300, 100, 100, self.x, self.y)
        else:
            self.image.clip_draw(self.frame * 100, 200, 100, 100, self.x, self.y)
        pass

class RUN:
    def enter(self, event):
        print('enter run')
        if event == RD: self.dir += 1
        elif event == LD : self.dir -= 1
        elif event == RU : self.dir -= 1
        elif event == LU : self.dir += 1

    def exit(self):
        print('exit run')
        #run울 나가서 idle로 갈때 run의 방향을 알려줗 필요가 있다.
        self.face_dir = self.dir
        pass

    def do(self):
        self.frame = (self.frame + 1) % 8
        self.x += self.dir
        self.x = clamp(0, self.x, 800) # 0 < self.x < 800
        pass

    def draw(self):
        if self.dir == -1:
            self.image.clip_draw(self.frame*100, 0, 100, 100, self.x, self.y)
        elif self.dir == 1:
            self.image.clip_draw(self.frame*100, 100, 100, 100, self.x, self.y)
        print(self.dir)
        pass



next_state = {
    AUTORUN : {RD:RUN, LD:RUN, RU:RUN, LU:RUN, AUTO:IDLE}, # 한쪽 키만 누른상태로 a를 누르면 안됨 누를꺼면 양쪽키를 누른상태에서 a를 눌러야함
    SLEEP : {RD:RUN, LD:RUN, RU:RUN, LU:RUN, SLEEP:SLEEP, AUTO:SLEEP}, # SLEEP:error_state
    IDLE : {RU:RUN, LU:RUN, RD:RUN, LD:RUN, TIMER: SLEEP, AUTO:AUTORUN}, # RU, LU는 동시에 입력시 떼었을떄 움직여야 하니 RUN
    RUN : {RU:IDLE, LU:IDLE, RD:IDLE, LD:IDLE, AUTO:AUTORUN}

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

    def __init__(self):
        self.x, self.y = 0, 90
        self.frame = 0
        self.dir, self.face_dir = 0, 1
        self.image = load_image('animation_sheet.png')

        self.q = []
        self.cur_state = IDLE
        self.cur_state.enter(self, None)

    def update(self):
        # self.frame = (self.frame + 1) % 8
        # self.x += self.dir * 1
        # self.x = clamp(0, self.x, 800)
        self.cur_state.do(self)

        if self.q: # q에 뭔가 들어있다면
            event = self.q.pop()        # event bring
            self.cur_state.exit(self)       # now state exit
            self.cur_state = next_state[self.cur_state][event]  # next state calculate
            self.cur_state.enter(self, event)      # next state enter

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
        self.cur_state.draw(self)

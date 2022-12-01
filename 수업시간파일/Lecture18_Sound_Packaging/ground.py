from pico2d import *

class Ground:
    def __init__(self):
        self.image = load_image('TUK_GROUND.png')
        # fill here
        self.bgm = load_music('football.mp3') # ogg라는 포멧으로 사용시 저작권료 불필요
        self.bgm.set_volume(32)
        self.bgm.repeat_play()

    def __getstate__(self):
        state = {}
        return state

    def __setstate__(self, state):
        self.__init__()

    def update(self):
        pass

    def draw(self):
        self.image.draw(1280 // 2, 1024 // 2)


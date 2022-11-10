from pico2d import *

class Grass:
    def __init__(self):
        self.image = load_image('grass.png')

    def update(self):
        pass

    def draw(self):
        self.image.draw(400, 30)
        self.image.draw(1200, 30)
        draw_rectangle(*self.get_bb())  # return 이 tuple이므로 *을 사용하면 풀어해침(4개의 변수로)

    def get_bb(self):
        return 0, 0, 1600 - 1, 50


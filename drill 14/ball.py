import server
import random
from pico2d import *
import game_world
import game_framework
import boy

class Ball:
    image = None
    def __init__(self):
        if Ball.image == None:
            Ball.image = load_image('ball21x21.png')

        self.x = random.randint(0, server.background.w - 1)
        self.y = random.randint(0, server.background.h - 1)

    def update(self):
        # self.x -= server.boy.x_velocity * game_framework.frame_time
        # self.y -= server.boy.y_velocity * game_framework.frame_time
        #
        # self.x = clamp(0, self.x, server.background.w - 1)
        # self.y = clamp(0, self.y, server.background.h - 1)
        # print(server.background.w, server.background.h)
        pass

    def draw(self):
        self.image.clip_draw(0, 0, 23, 23, self.x, self.y)

    def get_bb(self):
        return self.x - 11, self.y - 11, self.x + 11, self.y + 11

    def handle_collision(self, o, group):
        game_world.remove_collision_object(self)
        game_world.remove_object(self)
        server.boy.eat_count += 1
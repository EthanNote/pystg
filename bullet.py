import pygame

from axis import Axis
from utility import Utility


class Bullet(pygame.sprite.Sprite, dict):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image, self.rect = Utility.load_image_file('bullet.png')
        self.params = {}


class BulletDirector:
    def __init__(self):
        pass


class DemoBulletDirector:
    def __init__(self, start, end):
        self.start = start
        self.bullets = [Bullet() for i in range(10)]

    def update(self, time):
        for i in range(10):
            self.bullets[i]['x'] = i * 10 + 100
            self.bullets[i]['y'] = i
            pygame.transform()

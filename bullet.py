import pygame

from axis import Axis
from utility import Utility


class Bullet(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image, self.rect = Utility.load_image_file('bullet.png')
        self.params={}

class BulletDirector:
    def __init__(self):
        pass


class DemoBulletDirector:
    pass
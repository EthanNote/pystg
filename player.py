import pygame

from axis import Axis
from utility import Utility


class Player(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image, self.rect = Utility.load_image_file('player.png')
        grect = Utility.screen.get_rect()
        self.rect.x = (grect.width - self.rect.width) / 2
        self.rect.y = (grect.height - self.rect.height)
        self.axis = Axis()
        self.speed = 5
        self.speed_slow = 2

    def update(self, event, time):
        self.axis.update(event)
        v = self.axis.get_vector()
        if v[0] != 0 and v[1] != 0:
            v = (v[0] * 0.707, v[1] * 0.707)

        """Move player character """

        if self.axis.get_shift():
            print('shift')
            self.rect.move_ip((v[0] * self.speed_slow, v[1] * self.speed_slow))
        else:
            self.rect.move_ip((v[0] * self.speed, v[1] * self.speed))
        #self.rect.move_ip(1,1)
        grect = Utility.screen.get_rect()
        self.rect.x = max(0, min(self.rect.x, grect.width - self.rect.width))
        self.rect.y = max(0, min(self.rect.y, grect.height - self.rect.height))

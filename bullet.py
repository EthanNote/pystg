from math import sin, pi, cos

from pgzero import loaders
from pgzero.actor import Actor, POS_TOPLEFT, ANCHOR_CENTER

from handler import Handler


class Bullet(Actor):
    bullet_images = {}

    @classmethod
    def load(cls, fname):
        cls.bullet_images['.'.join(fname.split('.')[:-1])] = loaders.images.load(fname)

    def __init__(self, image, pos=POS_TOPLEFT, anchor=ANCHOR_CENTER, **kwargs):
        super().__init__(image, pos, anchor, **kwargs)

    @property
    def image(self):
        return self._image_name

    @image.setter
    def image(self, image):
        if image not in Bullet.bullet_images:
            raise Exception('image not loaded:', image)
        self._image_name = image
        self._orig_surf = self._surf = Bullet.bullet_images[image]
        self._update_pos()


class Firing(Handler):
    def __init__(self):
        self.frame_count = 0
        Bullet.load('bullet.png')
        self.bullets = [Bullet('bullet') for i in range(10)]
        for i in range(10):
            self.bullets[i].angle = i * 36
            self.bullets[i].pos = (sin(i * 36 * pi / 180) * (50 + self.frame_count * 0.2) + 400,
                                   cos(i * 36 * pi / 180) * (50 + self.frame_count * 0.2) + 300)

    def onUpdate(self, dt):
        for i in range(10):
            self.bullets[i].pos = (sin(i * 36 * pi / 180) * (50 + self.frame_count * 1) + 400,
                                   cos(i * 36 * pi / 180) * (50 + self.frame_count * 1) + 300)
        self.frame_count += 1

    def onDraw(self):
        #print(self.frame_count)
        for b in self.bullets:
            b.draw()
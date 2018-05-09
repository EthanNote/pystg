from pgzero import loaders
from pgzero.actor import Actor, POS_TOPLEFT, ANCHOR_CENTER


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


# class Firing:
#
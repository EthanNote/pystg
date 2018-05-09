from pgzero.actor import Actor

from bullet import Bullet
from handler import Handler
from stgame import STGame


class TestHandler(Handler):
    def __init__(self):
        Bullet.load('bullet.png')
        self.a = Bullet('bullet')

    def onUpdate(self, dt):
        self.a.angle += 1

    def onDraw(self):
        self.a.draw()

game = STGame()
game.run(TestHandler)

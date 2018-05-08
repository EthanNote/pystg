from pgzero.actor import Actor

from handler import Handler
from stgame import STGame


class TestHandler(Handler):
    def __init__(self):
        self.a = Actor('bullet.png')

    def onUpdate(self, dt):
        self.a.angle += 1

    def onDraw(self):
        self.a.draw()

game = STGame()
game.run(TestHandler)

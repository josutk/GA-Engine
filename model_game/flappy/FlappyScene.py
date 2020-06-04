from engine.Scene import Scene
from engine.GameObject import GameObject
from BackGround import BackGround
from LandScape import LandScape
from engine.Sprite import Sprite

class FlappyScene(Scene):

    def __init__(self, screen, id=0):
        super().__init__(screen, id)
    
    def load(self):
        self.backGround_1 = BackGround(self.screen, 0, 0, 0, 600)
        self.backGround_2 = BackGround(self.screen, 0, 0, 300, 600)
        self.landScape = LandScape(self.screen, 0, 0, 0, 0)
        self.landScape.load()
        self.backGround_1.load()
        self.backGround_1.load()
        self.backGround_2.load()
        self.backGround_2.load()

    def draw(self):
        self.backGround_1.draw()
        self.backGround_2.draw()
        self.landScape.draw()

    def update(self):
        self.backGround_1.update()
        self.backGround_2.update()
        self.landScape.update()        
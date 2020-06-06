from engine.GameObject import GameObject
from engine.Sprite import Sprite
from engine.KeyBoard import KeyBoard

class Pipe(GameObject):

    def __init__(self, screen, position_x, position_y, height, width):
        super().__init__(screen, position_x, position_y)
        self.sprite = Sprite('pipe-red.png', height, width, None)
        self.group = self.sprite.group()
        
    def load(self):
        self.group.add(self.sprite)
    
    def update(self):
       self.sprite.rect[0]-=1
       self.group.update()        
    def draw(self):
        self.group.draw(self.screen)
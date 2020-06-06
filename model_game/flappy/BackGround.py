from engine.Sprite import Sprite
from engine.GameObject import GameObject

class BackGround(GameObject):

    def __init__(self, screen, position_x, position_y, height, width):
        super().__init__(screen, 0, 0)
        self.sprite = Sprite('base.png', height, width, None)
        self.group = self.sprite.group()
        self.sprite.get_image()
    
    def load(self):
        self.group.add(self.sprite)
    
    def update(self):
        self.group.update()        

    def draw(self):
        self.group.draw(self.screen)

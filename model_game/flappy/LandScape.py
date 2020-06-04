from engine.GameObject import GameObject
from engine.Sprite import Sprite

class LandScape(GameObject):

    def __init__(self, screen, position_x, position_y, height, width):
        super().__init__(screen, 0, 0)
        self.sprite = Sprite('background-day.png', height, width, (600, 600))
        self.image = self.sprite.get_image()
        self.group = self.sprite.group()
    
    def load(self):
        self.group.add(self.sprite)
    
    def update(self):
        self.group.update()        

    def draw(self):
        self.group.draw(self.screen)


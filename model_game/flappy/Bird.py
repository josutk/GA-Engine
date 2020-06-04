from engine.GameObject import GameObject
from engine.Sprite import Sprite

class Bird(GameObject):

    def __init__(self, screen, position_x, position_y, height, width):
        super().__init__(screen, 0, 0)
        self.sprite_1 = Sprite('bluebird-upflap.png', height, width, None)
        self.sprite_2 = Sprite('bluebird-midflap.png', height, width, None)
        self.sprite_3 = Sprite('bluebird-downflap.png', height, width, None)
        
        self.group = self.sprite_1.group()
        self.sprites = [self.sprite_1, 
                        self.sprite_2, 
                        self.sprite_3
                        ]
        
        self.sprite_1_image = self.sprite_1.get_image()
        
        self.rect = self.sprite_1_image.get_rect()
        self.rect[0] = position_x
        self.rect[1] = position_y
    
    def load(self):
        self.group.add(self.sprite_1)
    
    def update(self):
        self.group.update()        

    def draw(self):
        self.group.draw(self.screen)

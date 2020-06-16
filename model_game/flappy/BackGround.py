from engine.Sprite import Sprite
from engine.GameObject import GameObject
import pygame
class BackGround(GameObject):

    def __init__(self, screen, position_x, position_y, height, width, inverted):
        super().__init__(screen, 0, 0)
        self.sprite = Sprite('base.png', height, width, None)
        #self.sprite.get_image()
        self.inverted = inverted
        if self.inverted:
            self.sprite.image = pygame.transform.flip(self.sprite.image, False, True)
        self.group = self.sprite.group()

    def load(self):
        self.group.add(self.sprite)
    
    def update(self):
        self.group.update()        

    def draw(self):
        self.group.draw(self.screen)

    
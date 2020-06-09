from engine.GameObject import GameObject
from engine.Sprite import Sprite
from engine.KeyBoard import KeyBoard
import pygame
class Pipe(GameObject):

    def __init__(self, screen, position_x, position_y, height, width, inverted):
        super().__init__(screen, position_x, position_y)
        
        self.sprite = Sprite('pipe-red.png', height, width, None)
        self.inverted = inverted
        if inverted:
            self.sprite.image = pygame.transform.flip(self.sprite.image, False, True)

        self.group = self.sprite.group()

    def load(self):
        self.group.add(self.sprite)
    
    def update(self):
       self.sprite.rect[0]-= 5 
       self.group.update()  
    
    def draw(self):
        self.group.draw(self.screen)
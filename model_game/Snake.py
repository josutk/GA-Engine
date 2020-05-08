import pygame
from engine.GameObject import GameObject
from engine.GameColors import GREEN

class Snake(GameObject):

    def __init__(self, screen, position_x, position_y):
        super().__init__(screen, position_x, position_y)
    
    def draw(self):        
        pygame.draw.rect(self.screen, GREEN, [self.position_x, 
                                        self.position_y,
                                        15,
                                        15])


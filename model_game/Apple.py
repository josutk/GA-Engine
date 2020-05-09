import pygame
from engine.GameObject import GameObject
from engine.GameColors import RED

class Apple(GameObject):

    def __init__(self, screen, position_x, position_y):
        super().__init__(screen, position_x, position_y)
    
    def draw(self):
        pygame.draw.rect(self.screen, RED, [self.position_x, 
                                        self.position_y,
                                        20,
                                        20])


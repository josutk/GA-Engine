import pygame
from engine.GameObject import GameObject
from engine.GameColors import BLACK
import copy

class Bar(GameObject):

    def __init__(self, screen, position_x, 
                               position_y,
                               height, width):
        
        super().__init__(screen, position_x, position_y)
        self.height = height
        self.width = width

    def draw(self):
        pygame.draw.rect(self.screen, BLACK, [self.position_x, 
                                        self.position_y,
                                        self.height,
                                        self.width])


import pygame
from engine.GameObject import GameObject
from engine.GameColors import BLUE
import copy

class Bar(GameObject):

    def __init__(self, screen, position_x, 
                               position_y,
                               height, width):
        
        super().__init__(position_x, position_y)
        self.screen = screen
        self.height = height
        self.width = width

    def draw(self):
        pygame.draw.rect(self.screen, BLUE, [self.position_x, 
                                        self.position_y,
                                        self.height,
                                        self.width])


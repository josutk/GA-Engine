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
        self.bar_rect = pygame.Rect(self.position_x, 
                                    self.position_y,
                                    self.height,
                                    self.width)

    def draw(self):
        pygame.draw.rect(self.screen, BLACK, self.bar_rect)
    
    def get_rect(self):
        return self.bar_rect


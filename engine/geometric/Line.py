import pygame
from engine.GameObject import GameObject

class Line(GameObject):
    def __init__(self, screen, position_x, position_y, color):
        super().__init__(screen, position_x, position_y)
        self.color = color
    
    def draw(self, end_position):
        pygame.draw.line(self.screen, 
                         self.color,
                         (self.position_x, self.position_y),
                          end_position )
import pygame
from engine.GameObject import GameObject

class Rectangule(GameObject):
    
    def __init__(self, screen, position_x, position_y, width, height, color):
        super().__init__(screen, position_x, position_y)
        self.color = color 
        self.rectangule = pygame.Rect(position_x, position_y, width, height)        
        
    def draw(self):
        pygame.draw.rect(self.screen, self.color, self.rectangule)

    def move_rectangule(self, axis_x, axis_y):
        self.rectangule.move_ip(axis_x, axis_y)

    def get_rectangule(self):
        return self.rectangule

    def get_width(self):
        return self.width
    
    def get_height(self):
        return self.height
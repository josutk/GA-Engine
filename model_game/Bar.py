import pygame
from engine.GameObject import GameObject
from engine.GameColors import BLACK
from engine.geometric.Rectangule import Rectangule

class Bar(Rectangule):

    def __init__(self, screen, position_x, 
                               position_y,
                               height, width):
        super().__init__(screen, position_x, position_y, width, height, BLACK)


import pygame
from engine.GameObject import GameObject
from engine.GameColors import RED
from engine.geometric.Rectangule import Rectangule

class Apple(Rectangule):

    def __init__(self, screen, position_x, position_y):
        super().__init__(screen, position_x, position_y, 20, 20, RED)
    

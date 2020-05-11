import pygame
from engine.GameObject import GameObject
from engine.GameColors import GREEN
from engine.KeyBoard import KeyBoard
from engine.geometric.Rectangule import Rectangule

class Snake(Rectangule):

    def __init__(self, screen, position_x, position_y):
        super().__init__(screen, position_x, position_y, 20, 20, GREEN)

    def update(self, right, left, top, botton):
        keyBoard = KeyBoard()
        for event in keyBoard.get_events():
             if event.type == keyBoard.KEYDOWN:
                if event.key == keyBoard.DOWN:
                    self.move_rectangule(0, botton)
                if event.key == keyBoard.UP:
                    self.move_rectangule(0, top)
                if event.key == keyBoard.LEFT:
                    self.move_rectangule(left, 0)
                if event.key == keyBoard.RIGHT:
                    self.move_rectangule(right, 0)
    
import pygame
from engine.GameObject import GameObject
from engine.GameColors import GREEN
from engine.KeyBoard import KeyBoard
from engine.geometric.Rectangule import Rectangule

class Snake(Rectangule):

    def __init__(self, screen, position_x, position_y):
        super().__init__(screen, position_x, position_y, 20, 20, GREEN)
        self.snake_body = [self]      
    
    def draw_snake(self):
        for block_body in self.snake_body:
            block_body.draw()
    
    def update(self, right, left, top, botton):
        keyBoard = KeyBoard()
        for event in keyBoard.get_events():
             if event.type == keyBoard.KEYDOWN:
                if event.key == keyBoard.DOWN:
                    self.move_rectangule(0, top)
                    new_position = self.position_y + top
                    self.set_position_y(new_position)
                if event.key == keyBoard.UP:
                    self.move_rectangule(0, botton)
                    new_position = self.position_y + botton
                    self.set_position_y(new_position)
                if event.key == keyBoard.LEFT:
                    self.move_rectangule(left, 0)
                    new_position = self.position_y + left
                    self.set_position_x(new_position)
                if event.key == keyBoard.RIGHT:
                    self.move_rectangule(right, 0)
                    new_position = self.position_y + right
                    self.set_position_x(new_position)
    
    def grow_body(self, position_x, position_y):
        body_part = Rectangule(self.screen, position_x, position_y, 20, 20, GREEN)
        self.snake_body.append(body_part)
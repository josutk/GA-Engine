import pygame
from engine.GameObject import GameObject
from engine.GameColors import GREEN
from engine.KeyBoard import KeyBoard
from engine.geometric.Rectangule import Rectangule

class Snake(Rectangule):

    def __init__(self, screen, position_x, position_y):
        super().__init__(screen, position_x, position_y, 20, 20, GREEN)
        self.snake_body = [self]      
        self.current_position = [self]

    def draw_snake(self):
        for block_body in self.snake_body:
            block_body.draw()
    
    def update(self, right, left, top, botton):
        keyBoard = KeyBoard()
        side = 1000
        for event in keyBoard.get_events():
             if event.type == keyBoard.KEYDOWN:
                if event.key == keyBoard.DOWN:
                    self.move_rectangule(0, top)
                    new_position = self.position_y + top
                    self.set_position_y(new_position)
                    side = 0
                if event.key == keyBoard.UP:
                    self.move_rectangule(0, botton)
                    new_position = self.position_y + botton
                    self.set_position_y(new_position)
                    side = 1
                if event.key == keyBoard.LEFT:
                    self.move_rectangule(left, 0)
                    new_position = self.position_x + left
                    self.set_position_x(new_position)
                    side = 2
                if event.key == keyBoard.RIGHT:
                    self.move_rectangule(right, 0)
                    new_position = self.position_x + right
                    self.set_position_x(new_position)
                    side = 3
    """
        for i in range(len(self.snake_body)):
            previous_x = self.snake_body[0].get_position()[0]
            previous_y = self.snake_body[0].get_position()[1]
            if i != 0:
                if side == 0 :
                    self.snake_body[i].set_position_x(previous_y)
                if side == 1:
                    self.snake_body[i].set_position_y(previous_y)
                if side == 2:
                    self.snake_body[i].set_position_y(previous_x)
                if side == 3:
                    self.snake_body[i].set_position_x(previous_x)
                
                self.snake_body[i].update()
    """
    def grow_body(self, position_x, position_y):
        body_part = Rectangule(self.screen, position_x, position_y, 20, 20, GREEN)
        self.snake_body.append(body_part)
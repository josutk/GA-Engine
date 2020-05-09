import pygame
from engine.GameObject import GameObject
from engine.GameColors import GREEN
from engine.KeyBoard import KeyBoard

class Snake(GameObject):

    def __init__(self, screen, position_x, position_y):
        super().__init__(screen, position_x, position_y)
        self.snake_rect = pygame.Rect(self.position_x, 
                                      self.position_y,
                                      20,
                                      20)

    def draw(self):        
        pygame.draw.rect(self.screen, GREEN, self.snake_rect)
        print(self.snake_rect) 
    def update(self):
        keyBoard = KeyBoard()
        for event in keyBoard.get_events():
             if event.type == keyBoard.KEYDOWN:
                if event.key == keyBoard.DOWN:
                    #self.position_y += 5
                    self.snake_rect.move_ip(0, 25)
                if event.key == keyBoard.UP:
                    #self.position_y -= 5
                    self.snake_rect.move_ip(0, -25)
                if event.key == keyBoard.LEFT:
                    #self.position_x -= 5
                    self.snake_rect.move_ip(-25, 0)
                if event.key == keyBoard.RIGHT:
                    #self.position_x += 5
                    self.snake_rect.move_ip(25, 0)
    
    def get_rect(self):
        return self.snake_rect
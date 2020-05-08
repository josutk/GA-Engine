import pygame
import random
from engine.Scene import Scene
from Bar import Bar
from Boundary import Boundary
from Snake import Snake
from Apple import Apple

class ExperimentalScene(Scene):

    def __init__(self,screen, id=0):
        super().__init__(screen, id)

    def random_position(self):
        x = random.randint(21, 379)
        y = random.randint(21, 379)
        return x, y

    def draw(self):
        boundary = Boundary(self.screen, 0, 0)
        
        snake_position_x, snake_position_y = self.random_position()   
        snake = Snake(self.screen, snake_position_x, snake_position_y)
        
        apple_position_x, apple_position_y = self.random_position()
        apple = Apple(self.screen, apple_position_x, apple_position_y)
        boundary.draw()
        apple.draw()
        snake.draw()
  
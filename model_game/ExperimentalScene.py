import pygame
import random
from engine.Scene import Scene
from engine.Collision import Collision
from Bar import Bar
from Boundary import Boundary
from Snake import Snake
from Apple import Apple


class ExperimentalScene(Scene):

    def __init__(self,screen, id=0):
        super().__init__(screen, id)

    def load(self):
        self.boundary = Boundary(self.screen, 0, 0)
        
        snake_position_x, snake_position_y = self.random_position()   
        self.snake = Snake(self.screen, snake_position_x, snake_position_y)
        
        apple_position_x, apple_position_y = self.random_position()
        self.apple = Apple(self.screen, apple_position_x, apple_position_y)
        self.collision = Collision(self.boundary.get_boundaries())

    def random_position(self):
        x = random.randint(21, 379)
        y = random.randint(21, 379)
        return x, y

    def draw(self):
        self.boundary.draw()
        self.apple.draw()
        self.snake.draw()
    
    def limit_movements(self):
        is_collider, object_collider = self.collision.check_collision(self.snake)
        if object_collider == self.boundary.horizontal_bar_left.get_rectangule(): 
            self.snake.update(25, 0, 25, -25)
        elif object_collider == self.boundary.horizontal_bar_right.get_rectangule():
            self.snake.update(0, -25, 25, -25)
        elif object_collider == self.boundary.vertical_bar_botton.get_rectangule(): 
             self.snake.update(25, -25, 0, -25)
        elif object_collider == self.boundary.vertical_bar_top.get_rectangule():
            self.snake.update(25, -25, 25, 0)
        else:
            self.snake.update(25, -25, 25, -25)

    def eat_apple(self):
        is_collider, object_collider = self.collision.check_collision(self.snake)
        if self.collision.object_colision(self.snake, self.apple):
            del self.apple
            new_x, new_y = self.random_position()
            self.apple = Apple(self.screen, new_x, new_y)

    
    def update(self):
        self.limit_movements()
        self.eat_apple()


from engine.GameObject import GameObject
from engine.Sprite import Sprite
from engine.KeyBoard import KeyBoard
import pygame
import math
from NeuralNetwork import NeuralNetwork

class Bird(GameObject):

    def __init__(self, screen, position_x, position_y, height, width):
        super().__init__(screen, position_x, position_y)
        self.sprite = Sprite('bluebird-upflap.png', height, width, None)
        self.group = self.sprite.group()
        self.position_y = position_y
        self.neuralNetwork = NeuralNetwork()
    
    def load(self):
        self.group.add(self.sprite)

    def update(self, params):
        value = self.neuralNetwork.predict([params])
        if value[0][0] > 0.5:
            flag_movement = 'down'
        else:
            flag_movement = 'up'
        self.movement(flag_movement)
        self.group.update()        

    def movement(self, flag):
        if flag == 'up':
            self.position_y = -10 + self.position_y
            self.sprite.set_position(self.position_y)
        else:
            self.position_y += 1
            self.sprite.set_position(self.position_y)
    
    def draw(self):
        self.group.draw(self.screen)


    def distance(self, sprite_object):
        dist = math.hypot(self.position_x-sprite_object.position_x, 
                          self.position_y-sprite_object.position_y)
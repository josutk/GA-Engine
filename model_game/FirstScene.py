from engine.Scene import Scene
from Bar import Bar
import pygame

class ExperimentalScene(Scene):

    def __init__(self, id=0):
        super().__init__(id)

    def draw(self, screen):
        horizontal_bar_right = Bar(screen, 0, 0, 400, 20)
        vertical_bar_top = Bar(screen, 0, 0, 20, 400)
        horizontal_bar_left = Bar(screen, 400, 380, -400, 20)
        vertical_bar_botton = Bar(screen, 380, 400, 20, -400 )
        
        horizontal_bar_left.draw()
        vertical_bar_botton.draw()
        vertical_bar_top.draw()
        horizontal_bar_right.draw()
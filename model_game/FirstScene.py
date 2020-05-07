from engine.Scene import Scene
from Bar import Bar
import pygame

class ExperimentalScene(Scene):

    def __init__(self, id=0):
        super().__init__(id)

    def draw(self, screen):
        bar = Bar(screen, 100, 100, 50, 20)
        bar.draw()
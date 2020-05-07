from engine.Scene import Scene
from Bar import Bar
import pygame
from Boundary import Boundary

class ExperimentalScene(Scene):

    def __init__(self, id=0):
        super().__init__(id)

    def draw(self, screen):
        boundary = Boundary(screen, 0, 0)
        boundary.draw()
from engine.Scene import Scene
from HorizontalBar import HorizontalBar
import pygame

class ExperimentalScene(Scene):

    def __init__(self, id=0):
        super().__init__(id)

    def draw(self, screen):
        bar = HorizontalBar(screen, 100, 100, 50, 20)
        bar.draw()
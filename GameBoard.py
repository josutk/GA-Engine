import pygame
import os 

class GameBoard:

    def __init__(self, height=0, weight=0):
        self.height = height
        self.weight = weight
        os.environ['SDL_VIDEO_WINDOW_POS'] = "%d,%d" % (500, 200)

    def start_board(self):
        screen = pygame.display.set_mode((self.height, self.weight))
        return screen

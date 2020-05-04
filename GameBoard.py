import pygame
class GameBoard:

    def __init__(self, height=0, weight=0):
        self.height = height
        self.weight = weight
    
    def start_board(self):
        screen = pygame.display.set_mode((self.height, self.weight))
        return screen

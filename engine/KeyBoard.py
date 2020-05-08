import pygame

class KeyBoard:

    KEYDOWN = pygame.KEYDOWN
    UP = pygame.K_UP
    DOWN = pygame.K_DOWN
    LEFT = pygame.K_LEFT
    RIGHT = pygame.K_RIGHT
   
    def __init__(self):
        self.events = pygame.event.get()

    def get_events(self):
        return self.events

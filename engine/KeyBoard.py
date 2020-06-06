import pygame

class KeyBoard:

    KEYDOWN = pygame.KEYDOWN
    UP = pygame.K_UP
    DOWN = pygame.K_DOWN
    LEFT = pygame.K_LEFT
    RIGHT = pygame.K_RIGHT
    SPACE = pygame.K_SPACE
   
    def __init__(self):
        self.events = pygame.event.get()
        self.keys = pygame.key.get_pressed()

    def get_events(self):
        return self.events

    def press_botton(self):
       return self.keys 
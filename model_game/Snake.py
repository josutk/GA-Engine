import pygame
from engine.GameObject import GameObject
from engine.GameColors import GREEN

class Snake(GameObject):

    def __init__(self, screen, position_x, position_y):
        super().__init__(screen, position_x, position_y)
    
    def draw(self):        
        pygame.draw.rect(self.screen, GREEN, [self.position_x, 
                                        self.position_y,
                                        15,
                                        15])
        #self.update()

    def update(self):
        events = pygame.event.get()
        for event in events:
             if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_DOWN:
                    self.position_y += 5
                    print('down')
                if event.key == pygame.K_UP:
                    self.position_y -= 5
                    print('up')
                if event.key == pygame.K_LEFT:
                    self.position_x -= 5
                    print('left')
                if event.key == pygame.K_RIGHT:
                    self.position_x += 5
                    print('right')
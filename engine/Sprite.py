import pygame

class Sprite(pygame.sprite.Sprite):
    
    def __init__(self, path, width, height, scale):        
        pygame.sprite.Sprite.__init__(self)
        self.path = path
        self.image = self.__convert_alpha()
        if (scale is not None):
            self.image = self.scale(scale)
        self.mask = pygame.mask.from_surface(self.image)
        self.rect = self.image.get_rect()
        self.rect[0] = width
        self.rect[1] = height

    def __convert_alpha(self):
        return pygame.image.load(self.path).convert_alpha()

    def group(self):
        return pygame.sprite.Group()
    
    def scale(self, scale):
        return pygame.transform.scale(self.image, scale)

    def get_image(self):
        return self.image

    def set_position(self, position):
        self.rect[1] = position
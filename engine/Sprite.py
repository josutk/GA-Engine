import pygame

class Sprite(pygame.sprite.Sprite):
    
    def __init__(self, path, width, height, scale):        
        pygame.sprite.Sprite.__init__(self)
        self.path = path
        self.image = self.__convert_alpha()
        self.scale_image = scale
        if (scale is not None):
            self.image = self.scale(self.scale_image)
        self.mask = pygame.mask.from_surface(self.image)
        self.rect = self.image.get_rect()
        self.rect[0] = width
        self.rect[1] = height

    def get_sprite_center(self):
        if self.scale_image == None:
            return self.rect[0], self.rect[1]
        else:
            x_pos_center = self.rect[0] + self.scale_image[0]/2
            y_pos_center = self.rect[1] + self.scale_image[1]/2
            return x_pos_center, y_pos_center
    
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
from engine.GameObject import GameObject
from engine.Sprite import Sprite
from engine.KeyBoard import KeyBoard

SPEED = 3
GRAVITY = 1
class Bird(GameObject):

    def __init__(self, screen, position_x, position_y, height, width):
        super().__init__(screen, position_x, position_y)
        self.sprite_1 = Sprite('bluebird-upflap.png', height, width, None)
        self.sprite_2 = Sprite('bluebird-midflap.png', height, width, None)
        self.sprite_3 = Sprite('bluebird-downflap.png', height, width, None)
        
        self.group = self.sprite_1.group()
        self.sprites = [self.sprite_1, 
                        self.sprite_2, 
                        self.sprite_3
                        ]
        
        self.sprite_1_image = self.sprite_1.get_image()
        self.position_y = position_y
    
    def load(self):
        self.group.add(self.sprite_1)
    
    def update(self):
        keyBoard = KeyBoard()
        flag_movement = 'down'
        for event in keyBoard.get_events():
            if event.type == keyBoard.KEYDOWN:
                if event.key == keyBoard.SPACE:
                    flag_movement = 'up'
        print(flag_movement)
        self.movement(flag_movement)
        self.group.update()        

    def movement(self, flag):
        if flag == 'up':
            self.position_y = -1
            self.sprite_1.set_position(self.position_y)
        else:
            self.position_y += GRAVITY
            self.sprite_1.set_position(self.position_y)
        
    def draw(self):
        self.group.draw(self.screen)

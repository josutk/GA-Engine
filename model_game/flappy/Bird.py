from engine.GameObject import GameObject
from engine.Sprite import Sprite
from engine.KeyBoard import KeyBoard

SPEED = 10
GRAVITY = 1
class Bird(GameObject):

    def __init__(self, screen, position_x, position_y, height, width):
        super().__init__(screen, position_x, position_y)
        self.sprite = Sprite('bluebird-upflap.png', height, width, None)
        
        self.group = self.sprite.group()
        
        self.position_y = position_y
    
    def load(self):
        self.group.add(self.sprite)
    
    def update(self):
        keyBoard = KeyBoard()
        flag_movement = 'down'
        for event in keyBoard.get_events():
            if event.type == keyBoard.KEYDOWN:
                if event.key == keyBoard.SPACE:
                    flag_movement = 'up'
        self.movement(flag_movement)
        self.group.update()        

    def movement(self, flag):
        if flag == 'up':
            self.position_y = -SPEED + self.position_y
            self.sprite.set_position(self.position_y)
        else:
            self.position_y += GRAVITY
            self.sprite.set_position(self.position_y)
    def draw(self):
        self.group.draw(self.screen)

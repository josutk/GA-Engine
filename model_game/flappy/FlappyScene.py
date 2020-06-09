from engine.Scene import Scene
from engine.GameObject import GameObject
from BackGround import BackGround
from LandScape import LandScape
from engine.Sprite import Sprite
from Bird import Bird
from Pipe import Pipe
from engine.Collision import Collision
from engine.geometric.Line import Line
from engine.GameColors import RED

class FlappyScene(Scene):

    def __init__(self, screen, id=0):
        super().__init__(screen, id)

    def load(self):
        self.backGround_1 = BackGround(self.screen, 0, 0, 0, 600)
        self.backGround_2 = BackGround(self.screen, 0, 0, 300, 600)
        self.landScape = LandScape(self.screen, 0, 0, 0, 0)
        
        self.bird = Bird(self.screen, 300, 400, 300, 400)
        self.pipe = Pipe(self.screen, 0, 0, 1200, 600, False)
        self.pipe_inverted = Pipe(self.screen, 0, 0, 1200, 0, True)
        self.landScape.load()
        self.backGround_1.load()
        self.backGround_2.load()
        self.bird.load()
        self.pipe.load()
        self.pipe_inverted.load()
        self.game_objects = [self.backGround_1, 
                                self.backGround_2, 
                                self.bird, 
                                self.pipe, 
                                self.pipe_inverted]
        self.collision_handler = Collision(self.game_objects)

    def draw(self):
        self.backGround_1.draw()
        self.backGround_2.draw()
        self.landScape.draw()
        self.bird.draw()
        self.pipe.draw()
        self.pipe_inverted.draw()

    def update(self):
    
        self.backGround_1.update()
        self.backGround_2.update()
        self.landScape.update()    
        self.bird.update()    
        self.pipe.update()
        self.pipe_inverted.update()

        pipe_center = self.pipe.sprite.get_sprite_center()
        pipe_inverted_center = self.pipe_inverted.sprite.get_sprite_center()
        bird_center = self.bird.sprite.get_sprite_center()
        backgroud_1_center = self.backGround_1.sprite.get_sprite_center()
        background_2_center = self.backGround_2.sprite.get_sprite_center()

        line_pipe = Line(self.screen,  pipe_center[0], pipe_center[1], RED)
        line_pipe_inve = Line(self.screen, pipe_inverted_center[0], pipe_inverted_center[1], RED)
        line_backGround_1 = Line(self.screen, backgroud_1_center[0], backgroud_1_center[1], RED)
        line_backGround_2 = Line(self.screen, background_2_center[0], background_2_center[1], RED)
        
        line_pipe.draw((bird_center))
        line_pipe_inve.draw((bird_center))
        line_backGround_1.draw((bird_center))
        line_backGround_2.draw((bird_center))
        
        if self.pipe.sprite.rect[0] <-self.pipe.sprite.rect[2]:
            del self.pipe
            self.pipe = Pipe(self.screen, 0, 0, 1200, 450, False)
            self.pipe.load()
        
        if self.pipe_inverted.sprite.rect[0] < -self.pipe_inverted.sprite.rect[2]:
            del self.pipe_inverted
            self.pipe_inverted = Pipe(self.screen, 0, 0, 1200, 0, True)
            self.pipe_inverted.load()

        if (self.collision_handler.sprite_group_collide(self.backGround_1.group, self.bird.group)) or (self.collision_handler.sprite_group_collide(self.backGround_2.group, self.bird.group)) or (self.collision_handler.sprite_group_collide(self.bird.group, self.pipe.group)) or (self.collision_handler.sprite_group_collide(self.pipe_inverted.group, self.bird.group)):
            input()

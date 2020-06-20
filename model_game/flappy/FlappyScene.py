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
import random
from GeneticAlgorithmFlappy import GeneticAlgorithmFlappy
from BirdException import BirdException
from NeuralNetwork import NeuralNetwork
import pygame

class FlappyScene(Scene):

    def __init__(self, screen, id=0):
        super().__init__(screen, id)

    def load(self, flag, generation_number):
        
        self.backGround_1 = BackGround(self.screen, 0, 0, 0, 600, False)
        self.backGround_2 = BackGround(self.screen, 0, 0, 300, 600, False)
        self.backGround_1_inverted = BackGround(self.screen, 0, 0, 0, 0, True)
        self.backGround_2_inverted = BackGround(self.screen, 0, 0, 300, 0, True)
        self.landScape = LandScape(self.screen, 0, 0, 0, 0)
        self.frame_alive = 0
        self.birds_pool = []
        self.bird_score = []
        self.models_load = []
        self.load_nn = [] 
        self.population_size = 8 
        self.generation_number = generation_number
        if flag:
            for idx in range(0, self.population_size):
                bird = Bird(self.screen, 300, 400, 300, 400)
                self.birds_pool.append(bird)
        else:
            for i in range(0, self.population_size):
                m = NeuralNetwork()
                self.load_nn.append(m)
                self.load_nn[i].get_model().load_weights("models/model" + str(i+1)+ ".keras")        
                bird = Bird(self.screen, 300, 400, 300, 400, self.load_nn[i])
                self.birds_pool.append(bird)
        
        self.pipe = Pipe(self.screen, 0, 0, 1200, 600, False)
        self.pipe_inverted = Pipe(self.screen, 0, 0, 1200, 0, True)
        self.landScape.load()
        self.backGround_1.load()
        self.backGround_2.load()
        self.backGround_1_inverted.load()
        self.backGround_2_inverted.load()
        
        self.nn = []
        for bird in self.birds_pool:
            bird.load()
        self.pipe.load()
        self.pipe_inverted.load()
        
        self.game_objects = [self.backGround_1, 
                                self.backGround_2, 
                                self.pipe, 
                                self.pipe_inverted,
                                self.backGround_1_inverted,
                                self.backGround_2_inverted] + self.birds_pool
        
        self.collision_handler = Collision(self.game_objects)
        
    def draw(self):
        self.landScape.draw()
        self.backGround_1.draw()
        self.backGround_2.draw()
        self.backGround_1_inverted.draw()
        self.backGround_2_inverted.draw()
        for bird in self.birds_pool:
            bird.draw()
        self.pipe.draw()
        self.pipe_inverted.draw()

    def update(self):
        if len(self.birds_pool) > 0:
            pipe_center = self.pipe.sprite.get_sprite_center()
            pipe_inverted_center = self.pipe_inverted.sprite.get_sprite_center()
            backgroud_1_center = self.backGround_1.sprite.get_sprite_center()
            background_2_center = self.backGround_2.sprite.get_sprite_center()
            backgroud_inverted_1_center = self.backGround_1_inverted.sprite.get_sprite_center()
            backgroud_inverted_2_center = self.backGround_2_inverted.sprite.get_sprite_center()
            
            self.backGround_1.update()
            self.backGround_2.update()
            self.backGround_2_inverted.update()
            self.backGround_1_inverted.update()
            self.landScape.update()    
            
            for bird in self.birds_pool:
                x, y = bird.get_position()
                bird.update([y, 
                            pipe_center[0] , 
                            pipe_center[1],
                            pipe_inverted_center[0],
                            pipe_inverted_center[1],
                            backgroud_1_center[0],
                            backgroud_1_center[1],
                            background_2_center[0],
                            background_2_center[1],
                            backgroud_inverted_1_center[0],
                            backgroud_inverted_1_center[1],
                            backgroud_inverted_2_center[0],
                            backgroud_inverted_2_center[1]
                            ])    
                bird_center = bird.sprite.get_sprite_center()
                line_pipe = Line(self.screen,  pipe_center[0], pipe_center[1], RED)
                line_pipe_inve = Line(self.screen, pipe_inverted_center[0], pipe_inverted_center[1], RED)
                line_backGround_1 = Line(self.screen, backgroud_1_center[0], backgroud_1_center[1], RED)
                line_backGround_2 = Line(self.screen, background_2_center[0], background_2_center[1], RED)

                line_backGround_inverted_1 = Line(self.screen, backgroud_inverted_1_center[0], backgroud_inverted_1_center[1], RED)
                line_backGround_inverted_2 = Line(self.screen, backgroud_inverted_2_center[0], backgroud_inverted_2_center[1], RED)

                line_pipe.draw((bird_center))
                line_pipe_inve.draw((bird_center))
                line_backGround_1.draw((bird_center))
                line_backGround_2.draw((bird_center))
                line_backGround_inverted_1.draw((bird_center))
                line_backGround_inverted_2.draw((bird_center))
                if (self.collision_handler.sprite_group_collide(self.backGround_1.group, bird.group)) or (self.collision_handler.sprite_group_collide(self.backGround_1_inverted.group, bird.group)) or (self.collision_handler.sprite_group_collide(self.backGround_2_inverted.group, bird.group)) or (self.collision_handler.sprite_group_collide(self.backGround_2.group, bird.group)) or (self.collision_handler.sprite_group_collide(bird.group, self.pipe.group)) or (self.collision_handler.sprite_group_collide(self.pipe_inverted.group, bird.group)):
                    self.nn.append(bird.get_neural_network())
                    self.bird_score.append(self.frame_alive)
                    self.birds_pool.remove(bird)
            
            self.pipe.update()
            self.pipe_inverted.update()

            y1 = random.randint(450, 500)
            y2 = random.randint(0, 100)
                
            if self.pipe.sprite.rect[0] < -self.pipe.sprite.rect[2]:
                del self.pipe
                self.pipe = Pipe(self.screen, 0, 0, 600, y1, False)
                self.pipe.load()

            if self.pipe_inverted.sprite.rect[0] < -self.pipe_inverted.sprite.rect[2]:
                del self.pipe_inverted
                self.pipe_inverted = Pipe(self.screen, 0, 0, 600, y2, True)
                self.pipe_inverted.load()
            self.frame_alive +=1
        else:
            new_birds = []
            self.geneticAlgorithmFlappy = GeneticAlgorithmFlappy(self.nn)
            self.geneticAlgorithmFlappy.template(self.bird_score)
            for idx in range(0, int(self.population_size/2)):
                bird = Bird(self.screen, 300, 400, 300, 400)
                new_birds.append(bird)
            self.geneticAlgorithmFlappy.new_population(new_birds)
            self.geneticAlgorithmFlappy.save()
            raise BirdException
        
        show_score = 0
        if len(self.bird_score) > 0:
            show_score = max(self.bird_score)
    
        font = pygame.font.Font('freesansbold.ttf', 11) 
        message = "Geração = " + str(self.generation_number) + " "\
                  "Quantidade de individuos vivos = " + str(len(self.birds_pool)) + " "  \
                  "Maior quantidade de frames vivos = " + str(show_score) 
        text = font.render(message, True, (0, 0, 0))
        self.screen.blit(text, (25, 25))
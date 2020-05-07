import pygame
import sys
from model_game.FirstScene import ExperimentalScene

class GameEngine:

	def __init__(self, screen):
		self.screen = screen
	
	def run(self):
		pygame.init()
		scene = ExperimentalScene(0)		
		scene.draw(self.screen)
		while True:
			for event in pygame.event.get(): 
				if event.type == pygame.QUIT:
					sys.exit()
			pygame.display.flip()

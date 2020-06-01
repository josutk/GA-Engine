import pygame
import sys
#from model_game.ExperimentalScene import ExperimentalScene

class GameEngine:

	def __init__(self, screen, scene):
		self.screen = screen
		self.scene = scene	
	
	def run(self):
		pygame.init()
		#scene = ExperimentalScene(self.screen, 0)		
		self.scene.load()
		while True:
			self.screen.fill((255,255,255))
			self.scene.draw()
			self.scene.update()
			for event in pygame.event.get(): 
				if event.type == pygame.QUIT:
					sys.exit()
			pygame.display.update()
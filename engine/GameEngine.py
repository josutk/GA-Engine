import pygame
import sys

class GameEngine:

	def __init__(self, screen, scene):
		self.screen = screen
		self.scene = scene	
	
	def run(self):
		pygame.init()
		clock = pygame.time.Clock()
		self.scene.load()
		while True:
			clock.tick(60)
			self.screen.fill((255,255,255))
			self.scene.draw()
			self.scene.update()
			for event in pygame.event.get(): 
				if event.type == pygame.QUIT:
					sys.exit()
			pygame.display.update()
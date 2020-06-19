import pygame
import sys
#import BirdException
from copy import copy 

class GameEngine:

	def __init__(self, screen, scene):
		self.screen = screen
		self.scene = scene	
		self.screen_copy = copy(screen)

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

	def run_continuos(self):
		pygame.init()
		clock = pygame.time.Clock()
		self.scene.load()
		reload_scene = False
		while True:
			clock.tick(60)
			try:
				if reload_scene:
					self.scene.load()
					reload_scene = False
				self.scene.draw()
				self.scene.update()
				for event in pygame.event.get(): 
					if event.type == pygame.QUIT:
						sys.exit()
				pygame.display.update()
			except Exception:
				reload_scene = True
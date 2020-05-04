import pygame
import sys
from GameBoard import GameBoard

class GameEngine:

	def run():
		pygame.init()
		gameBoard = GameBoard(400, 400)
		gameBoard.start_board()
		while True:
			for event in pygame.event.get(): 
				if event.type == pygame.QUIT:
					sys.exit()
			pygame.display.flip()

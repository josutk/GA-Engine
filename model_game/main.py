import sys
sys.path.insert(0, '../')

from engine.GameEngine import GameEngine
from engine.GameBoard import GameBoard

print(sys.path)

gameBoard = GameBoard(400, 400)
screen = gameBoard.start_board()

gameEngine = GameEngine(screen)
gameEngine.run()
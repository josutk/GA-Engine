import sys
sys.path.insert(0, '../')

from engine.GameEngine import GameEngine
from engine.GameBoard import GameBoard
from engine.GameColors import WHITE

print(sys.path)

gameBoard = GameBoard(400, 400)
screen = gameBoard.start_board()
gameBoard.set_board_color(WHITE)
gameEngine = GameEngine(screen)
gameEngine.run()
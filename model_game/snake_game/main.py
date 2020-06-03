import sys
sys.path.insert(0, '../../')

from engine.GameEngine import GameEngine
from engine.GameBoard import GameBoard
from engine.GameColors import WHITE
from ExperimentalScene import ExperimentalScene
print(sys.path)

gameBoard = GameBoard(400, 400)
screen = gameBoard.start_board()
gameBoard.set_board_color(WHITE)
scene = ExperimentalScene(screen, 0)		
gameEngine = GameEngine(screen, scene)
gameEngine.run()
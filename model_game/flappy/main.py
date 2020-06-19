import sys
sys.path.insert(0, '../../')

from engine.GameEngine import GameEngine
from engine.GameBoard import GameBoard
from engine.Scene import Scene
from FlappyScene import FlappyScene

gameBoard = GameBoard(600, 800)
screen = gameBoard.start_board()
scene =  FlappyScene(screen, 0)
gameEngine = GameEngine(screen, scene)
gameEngine.run_continuos()
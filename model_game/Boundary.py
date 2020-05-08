from engine.GameObject import GameObject
from Bar import Bar
class Boundary(GameObject):

    def __init__(self, screen, position_x, position_y):
        super().__init__(screen, position_x, position_y)
    
    def draw(self):
        horizontal_bar_right = Bar(self.screen, 0, 0, 400, 20)
        vertical_bar_top = Bar(self.screen, 0, 0, 20, 400)
        horizontal_bar_left = Bar(self.screen, 400, 380, -400, 20)
        vertical_bar_botton = Bar(self.screen, 380, 400, 20, -400)
        
        horizontal_bar_left.draw()
        vertical_bar_botton.draw()
        vertical_bar_top.draw()
        horizontal_bar_right.draw()
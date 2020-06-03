from Bar import Bar
from engine.GameObject import GameObject

class Boundary(GameObject):

    def __init__(self, screen, position_x, position_y):
        super().__init__(screen, position_x, position_y)
        self.vertical_bar_top = Bar(self.screen, 0, 0, 20, 400)
        self.horizontal_bar_left = Bar(self.screen, 0, 0, 400, 20)
        self.vertical_bar_botton = Bar(self.screen, 0, 380, 20, 400)
        self.horizontal_bar_right = Bar(self.screen, 380, 0, 380, 20)
    
    def draw(self):
        self.horizontal_bar_left.draw()
        self.vertical_bar_botton.draw()
        self.vertical_bar_top.draw()
        self.horizontal_bar_right.draw()
    
    def get_boundaries(self):
        return [self.horizontal_bar_left.get_rectangule(), 
                self.horizontal_bar_right.get_rectangule(), 
                self.vertical_bar_botton.get_rectangule(),
                self.vertical_bar_top.get_rectangule()]
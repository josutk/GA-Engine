class GameObject:

    def __init__(self, position_x, position_y):
        self.position_x = position_x
        self.position_y = position_y
    
    def draw(self):
        pass

    def update(self):
        pass
    
    def set_position_x(self, position_x):
        self.position_x = position_x

    def set_position_y(self, position_y):
        self.position_y = position_y

    def get_position(self):
        return self.position_x, self.position_y

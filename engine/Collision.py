class Collision:
    
    def __init__(self, game_objects_list):
        self.game_objects_list = game_objects_list
    
    def check_collision(self, object):
        if object.get_rect().collidelist(self.game_objects_list)>=0:
            print(self.game_objects_list)
            return True
        else:
             return False

    
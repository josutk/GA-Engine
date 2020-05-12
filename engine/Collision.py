class Collision:
    
    def __init__(self, game_objects_list):
        self.game_objects_list = game_objects_list
    
    def check_collision(self, object):
        if object.get_rectangule().collidelist(self.game_objects_list)>=0:
            object_collider = self._get_collider_object(object)
            return True, object_collider
        else:
             return False, None

    def _get_collider_object(self, object): 
        for game_object in self.game_objects_list:
            if object.get_rectangule().colliderect(game_object):
                return game_object

    def object_colision(self, colliding_object, collided_object):
        if colliding_object.get_rectangule().colliderect(collided_object.get_rectangule()):
            return True
        else:
            return False

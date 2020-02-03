from vector import Vector
from game_map import GameMap
import math 

class Player:
    def __init__(self, position_x, position_y):
        self.position = Vector(position_x, position_y)  # player's position on a map
        self.direction = Vector(0, 1)  # direction is a vector where player looks
        self.plane = Vector(0.66, 0)  # plane is a vector of camera plane
        self.way = Vector(0, 0)  # way is a vector where player moves
        self.angle = 0  # angle of rotation

    def move(self):
        self.position.x += self.way.x 
        self.position.y += self.way.y
        self.way.x = 0
        self.way.y = 0

    def rotate(self):  # from rotation matrix
        ------ counter clockwise ------
        x_direction = (self.direction.x * math.cos(self.angle)) - (self.direction.y * math.sin(self.angle))
        y_direction = (self.direction.x * math.sin(self.angle)) + (self.direction.y * math.cos(self.angle))
        self.direction.x = x_direction
        self.direction.y = y_direction
        x_plane = (self.plane.x * math.cos(self.angle)) - (self.plane.y  * math.sin(self.angle))
        y_plane = (self.plane.x * math.sin(self.angle)) + (self.plane.y  * math.cos(self.angle))
        self.plane.x = x_plane
        self.plane.y = y_plane
    

        
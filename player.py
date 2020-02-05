from vector import Vector
from game_map import GameMap
import math 


game_map = GameMap()

class Player:
    def __init__(self, position_x, position_y):
        self.position = Vector(position_x, position_y)  # player's position on a map
        self.direction = Vector(1, 0)  # direction is a vector where player looks
        self.plane = Vector(0, 0.66)  # plane is a vector of camera plane
        self.way = Vector(0, 0)  # way is lenght of player's step
        self.angle = 0  # angle of rotation

    def move(self):
        if game_map.maze[int(self.position.y + self.way.y * self.direction.y)][int(self.position.x + self.way.x * self.direction.x)] != 'X': 
            self.position.x += self.way.x * self.direction.x 
            self.position.y += self.way.y * self.direction.y
            self.way.x = 0
            self.way.y = 0

    def rotate(self):  # from rotation matrix
        x_direction = (self.direction.x * math.cos(self.angle)) - (self.direction.y * math.sin(self.angle))
        y_direction = (self.direction.x * math.sin(self.angle)) + (self.direction.y * math.cos(self.angle))
        self.direction.x = x_direction
        self.direction.y = y_direction
        x_plane = (self.plane.x * math.cos(self.angle)) - (self.plane.y  * math.sin(self.angle))
        y_plane = (self.plane.x * math.sin(self.angle)) + (self.plane.y  * math.cos(self.angle))
        self.plane.x = x_plane
        self.plane.y = y_plane
        self.angle = 0
        

        
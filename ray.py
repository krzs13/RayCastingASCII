from vector import Vector


class Ray:
    def __init__(self, position_x, position_y):
        self.position = Vector(position_x, position_y)  # start of the ray is same as player's position
        self.direction = Vector(0, 0)
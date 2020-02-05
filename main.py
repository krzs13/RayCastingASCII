from get_key import GetKey, Wait, ClearConsole, WindowSize
from game_map import GameMap
from screen import Screen
from player import Player
from ray import Ray
from vector import Vector
import math


if __name__ == '__main__':
    get_key = GetKey()
    game_map = GameMap()
    screen = Screen()
    player = Player(2 , 2)
    ray = Ray(player.position.x, player.position.y)
    WindowSize()

    while True:
        ClearConsole()
        screen.cleaner()

        key = get_key()
        if key == 27:
            break
        elif key == 299:  # left arrow - (rotation)
            player.angle = -0.2
        elif key == 301:  # right arrow - (rotation)
            player.angle = 0.2
        elif key == 296:  # up arrow - (step)
            player.way.x = 0.5  # collision detection
            player.way.y = 0.5
        elif key == 304:  # down arrow (step)
            player.way.x = -0.5
            player.way.y = -0.5
        player.move()
        player.rotate()

        # ====== RAY CASTING ======
        # ------ rays creation ------
        for x in range(0, 100):  # as many rays as characters in screen width
            map_x = int(player.position.x)  # box of the map where player is
            map_y = int(player.position.y)
            camera = (2 * (x / 99)) - 1  # left side of a screen is -1, center 0, right 1
            ray.direction.x = player.direction.x + (player.plane.x * camera)
            ray.direction.y = player.direction.y + (player.plane.y * camera)
            distance_x = 0  # length of ray from player's position to next x or y side of a box 
            distance_y = 0
            delta_distance_x = abs(1 / ray.direction.x)  # length of ray from one x or y side to next
            delta_distance_y = abs(1 / ray.direction.y)
            step_x = 0  # direction of ray's step on map's boxes (+1 or -1)
            step_y = 0
            wall_hit = 0
            site = 0
            # ------ first step of ray on a map ------
            if ray.direction.x < 0:  # calculate ray's step on map's boxes and distance_x or y
                step_x = -1
                distance_x = (player.position.x - map_x) * delta_distance_x
            else:
                step_x = 1
                distance_x = (map_x + 1 - player.position.x) * delta_distance_x
            if ray.direction.y < 0:
                step_y = - 1
                distance_y = (player.position.y - map_y) * delta_distance_y
            else:
                step_y = 1
                distance_y = (map_y + 1 - player.position.y) * delta_distance_y
            # ------ ray's further way on a map ------
            while wall_hit == 0:  # alghoritm that moves rays through map's boxes until it hits a wall 
                if distance_x < distance_y:  # choose x or y direction to move ray through map's boxes
                    distance_x += delta_distance_x
                    map_x += step_x
                    side = 0
                else:
                    distance_y += delta_distance_y
                    map_y += step_y
                    side = 1
                if game_map.maze[map_y][map_x] == 'X':
                    wall_hit = 1
            # ------ distance between player and wall ------
            wall_distance = 0
            if side == 0:
                wall_distance = (map_x - player.position.x + ((1 - step_x) / 2)) / ray.direction.x 
            else:
                wall_distance = (map_y - player.position.y + ((1 - step_y) / 2)) / ray.direction.y
            # ------ height of a wall printed on screen ------
            if wall_distance == 0:
                wall_height = 25
            else:
                wall_height = int(25 / wall_distance)  # 25 is screen's height 
            wall_start = int((-wall_height / 2) + (25 / 2))
            if wall_start < 0:
                wall_start = 0
            wall_end = int((wall_height / 2) + (25 / 2))
            if wall_end >= 25:
                wall_end = 25
            if wall_distance < 3:
                for y in range(wall_start, wall_end):
                    screen.screen[y][x] = u'\u2593'
            elif 3 <= wall_distance < 6:
                for y in range(wall_start, wall_end):
                    screen.screen[y][x] = u'\u2592'
            else:
                for y in range(wall_start, wall_end):
                    screen.screen[y][x] = u'\u2591'  
        screen.printer()       
        Wait()

    
from get_key import GetKey, Wait, ClearConsole, WindowSize
from game_map import GameMap
from screen import Screen
from player import Player
from ray import Ray
from vector import Vector


if __name__ == '__main__':
    get_key = GetKey()
    game_map = GameMap()
    screen = Screen()
    player = Player(5, 5)
    ray = Ray(player.position.x, player.position.y)
    WindowSize()

    while True:
        ClearConsole()
        screen.cleaner()

        # ====== RAY CASTING ======
        # ------ rays algorithm ------        
        for x in range(1, 101):  # as many steps as characters in screen width
            camera = (2 * (x / 100)) - 1  # left side of a screen is -1, center 0, right 1
            ray.direction.x = player.direction.x + (player.plane.x * camera)
            ray.direction.y = player.direction.y + (player.plane.y * camera)



        screen.printer()       
        Wait()

    
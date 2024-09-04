from typing import List


class Solution:

    def __moveNorth(self, x, y):
        return x, y + 1

    def __moveSouth(self, x, y):
        return x, y - 1

    def __moveWest(self, x, y):
        return x - 1, y

    def __moveEast(self, x, y):
        return x + 1, y

    def robotSim(self, commands: List[int], obstacles: List[List[int]]) -> int:
        direction_dict = {
            0: self.__moveNorth,
            1: self.__moveEast,
            2: self.__moveSouth,
            3: self.__moveWest
        }
        obstacles_dict = set((x[0], x[1]) for x in obstacles)
        direction = 0
        distance = 0
        x, y = 0, 0
        for command in commands:
            if command == -2:
                direction = (direction + 3) % 4
            elif command == -1:
                direction = (direction + 1) % 4
            else:
                for _ in range(command):
                    new_x, new_y = direction_dict[direction](x, y)
                    if (new_x, new_y) in obstacles_dict:
                        break
                    x, y = new_x, new_y

                distance = max(distance, x ** 2 + y ** 2)

        return distance
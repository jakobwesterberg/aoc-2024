import argparse
from enum import Enum

class Direction(Enum):
    N = 1,
    S = 2,
    W = 3,
    E = 4,

def walk(pos, obstacles):
    visited = {}
    loop = False

    while True:
        x, y, dir = pos
        match dir:
            case Direction.N:
                if y - 1 < 0:
                    break
                elif (x, y - 1) in obstacles:
                    pos = (x, y, Direction.E)
                else:
                    pos = (x, y - 1, dir)
                    if pos in visited:
                        loop = True
                        break
                    visited[pos] = True
            case Direction.S:
                if y + 1 == map_height:
                    break
                elif (x, y + 1) in obstacles:
                    pos = (x, y, Direction.W)
                else:
                    pos = (x, y + 1, dir)
                    if pos in visited:
                        loop = True
                        break
                    visited[pos] = True
            case Direction.W:
                if x - 1 < 0:
                    break
                elif (x - 1, y) in obstacles:
                    pos = (x, y, Direction.N)
                else:
                    pos = (x - 1, y, dir)
                    if pos in visited:
                        loop = True
                        break
                    visited[pos] = True
            case Direction.E:
                if x + 1 == map_width:
                    break
                elif (x + 1, y) in obstacles:
                    pos = (x, y, Direction.S)
                else:
                    pos = (x + 1, y, dir)
                    if pos in visited:
                        loop = True
                        break
                    visited[pos] = True

    return visited, loop

if __name__ == '__main__':
    arg_parser = argparse.ArgumentParser()
    arg_parser.add_argument('file')
    args = arg_parser.parse_args()

    with open(args.file) as file:
        s = file.read()
        s = s.split('\n')

        map_height = len(s)
        map_width = len(s[0])
        pos = None
        obstacles = {}
        for y in range(0, len(s)):
            for x in range(0, len(s[0])):
                c = s[y][x]
                if c == '#':
                    obstacles[(x, y)] = True
                elif c == '^':
                    pos = (x, y, Direction.N)

        visited, _ = walk(pos, obstacles)
        print(len(set([(x, y) for x, y, _ in visited])))

        new_obstacles = 0
        for y in range(0, map_height):
            for x in range(0, map_width):
                obstacles_updated = obstacles.copy()
                obstacles_updated[(x, y)] = True
                _, loop = walk(pos, obstacles_updated)
                if loop:
                    new_obstacles += 1

        print(new_obstacles)


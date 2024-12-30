import argparse
import math

def dijkstra(g, s):
    dist = {}
    prev = {}
    q = []

    for v in g:
        prev[v] = None
        dist[v] = math.inf
        q.append(v)

    dist[s] = 0

    while q:
        u = q[0]
        for v in q:
            if dist[v] < dist[u]:
                u = v

        q.remove(u)

        y, x, dir = u
        dy, dx = dir

        next_moves = []
        if dy:
            next_moves = [(y + dy, x, dir), (y, x, (0, 1)), (y, x, (0, -1))]
        elif dx:
            next_moves = [(y, x + dx, dir), (y, x, (1, 0)), (y, x, (-1, 0))]

        for v in next_moves:
            if v not in g:
                continue

            y_new, x_new, dir_new = v

            alt = dist[u]

            if ((y, x) == (y_new, x_new)):
                alt += 1000
            else:
                alt += 1

            if alt < dist[v]:
                dist[v] = alt
                prev[v] = u

    return dist, prev

if __name__ == '__main__':
    arg_parser = argparse.ArgumentParser()
    arg_parser.add_argument('file')
    args = arg_parser.parse_args()

    s = ""
    with open(args.file) as file:
        s = file.read()

    s = s.split('\n')

    maze = []
    start = None
    ends = None

    for i in range(0, len(s)):
        for j in range(0, len(s[0])):
            if s[i][j] == '.':
                maze.append((i, j, (1, 0)))
                maze.append((i, j, (-1, 0)))
                maze.append((i, j, (0, 1)))
                maze.append((i, j, (0, -1)))
            elif s[i][j] == 'S':
                start = (i, j, (0, 1))
                maze.append((i, j, (1, 0)))
                maze.append((i, j, (-1, 0)))
                maze.append((i, j, (0, 1)))
                maze.append((i, j, (0, -1)))
            elif s[i][j] == 'E':
                ends = [(i, j, (1, 0)), (i, j, (-1, 0)), (i, j, (0, 1)), (i, j, (0, -1))]
                maze.append((i, j, (1, 0)))
                maze.append((i, j, (-1, 0)))
                maze.append((i, j, (0, 1)))
                maze.append((i, j, (0, -1)))

    dist_start, prev = dijkstra(maze, start)
    shortest = math.inf
    shortest_end = None
    for end in ends:
        if dist_start[end] < shortest:
            shortest_end = end
            shortest = dist_start[end]

    print(shortest)

    dist_ends = []
    for end in ends:
        dist_end, _ = dijkstra(maze, end)
        dist_ends.append(dist_end)

    best_tiles = set()
    for v in maze:
        d_s = dist_start[v]
    
        for dist_end in dist_ends:
            d_e = dist_end[v]
            if d_s + d_e - 2000 == shortest:
                y, x, _ = v
                best_tiles.add((y, x))

    count = 0
    for v in best_tiles:
        if v == (start[0], start[1]):
            count += 1
            continue
        if v == (ends[0][0], ends[0][1]):
            count += 1
            continue

        n = 0
        if (v[0] + 1, v[1]) in best_tiles:
            n += 1
        if (v[0] - 1, v[1]) in best_tiles:
            n += 1
        if (v[0], v[1] + 1) in best_tiles:
            n += 1
        if (v[0], v[1] - 1) in best_tiles:
            n += 1

        if n >= 2:
            count += 1

    print(count)

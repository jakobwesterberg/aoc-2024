import argparse
import math

def min_dist(q, dist):
    v = q[0]

    for w in q:
        if dist[w] < dist[v]:
            v = w

    return v

def dijkstra(g, width, height):
    dist = {}
    q = []

    for i in range(height):
        for j in range(width):
            if (j, i) not in g:
                dist[(j, i)] = math.inf
                q.append((j, i))

    dist[(0, 0)] = 0

    while q:
        u = min_dist(q, dist)
        q.remove(u)

        for dy in [-1, 0, 1]:
            for dx in [-1, 0, 1]:
                if dy and dx:
                    continue
                x, y = u
                v = (x + dx, y + dy)
                if v in g:
                    continue

                if v[0] < 0 or v[1] < 0 or v[0] >= width or v[1] >= height:
                    continue

                alt = dist[u] + 1
                if alt < dist[v]:
                    dist[v] = alt

    return dist

if __name__ == '__main__':
    arg_parser = argparse.ArgumentParser()
    arg_parser.add_argument('file')
    args = arg_parser.parse_args()

    s = ""
    with open(args.file) as file:
        s = file.read()

    s = s.split('\n')

    bytes = []
    for line in s:
        i = 0
        second = False
        x = ""
        y = ""
        while i < len(line):
            if line[i] == ',':
                second = True
                i += 1
            elif second:
                while i < len(line) and line[i].isdigit():
                    y += line[i]
                    i += 1
                y = int(y)
            else:
                while i < len(line) and line[i].isdigit():
                    x += line[i]
                    i += 1
                x = int(x)
        bytes.append((x, y))

    test = args.file == "18.input.test"

    width = 71
    height = 71

    end = (70, 70)

    if test:
        width = 7
        height = 7

        end = (6, 6)

    if test:
        dist = dijkstra(bytes[0:12], width, height)
        print(dist[end])
    else:
        dist = dijkstra(bytes[0:1024], width, height)
        print(dist[end])

    for i in range(len(bytes), 0, -1):
        dist = dijkstra(bytes[0:i], width, height)
        if dist[end] != math.inf:
            print("{},{}".format(bytes[i][0], bytes[i][1]))
            break


import argparse
import math

def dijkstra(g, s):
    dist = {}
    prev = {}
    q = []

    for v in g:
        dist[v] = math.inf
        q.append(v)

    dist[s] = 0

    while q:
        u = q[0]
        for v in q:
            if dist[v] < dist[u]:
                u = v

        q.remove(u)

        for dy in [-1, 0, 1]:
            for dx in [-1, 0, 1]:
                if dy != 0 and dx != 0:
                    continue
                if dy == 0 and dx == 0:
                    continue

                y, x = u
                v = (y + dy, x + dx)

                if v not in g:
                    continue

                alt = dist[u] + 1
                if alt < dist[v]:
                    dist[v] = alt
                    prev[v] = u

    return dist, prev

def find_cheats(roads, start, end, ps):
    dist_start, prev_start = dijkstra(roads, start)
    dist_end, prev_end = dijkstra(roads, end)

    base = dist_start[end]
    cheats = {}

    v = start
    while v != end:
        w = end
        while v != w:
            delta_y = abs(v[0] - w[0])
            delta_x = abs(v[1] - w[1])
            
            if delta_y + delta_x <= ps:
                delta = base - (dist_start[v] + dist_end[w] + delta_y + delta_x)
                if delta > 0:
                    if delta in cheats:
                        cheats[delta] += 1
                    else:
                        cheats[delta] = 1

            w = prev_start[w]
        v = prev_end[v]

    return cheats

if __name__ == '__main__':
    arg_parser = argparse.ArgumentParser()
    arg_parser.add_argument('file')
    args = arg_parser.parse_args()

    s = ""
    with open(args.file) as file:
        s = file.read()
    s = s.split('\n')

    roads = []
    start = None
    end = None

    for i in range(0, len(s)):
        for j in range(0, len(s[0])):
            if s[i][j] == '.':
                roads.append((i, j))
            elif s[i][j] == 'S':
                start = (i, j)
                roads.append((i, j))
            elif s[i][j] == 'E':
                end = (i, j)
                roads.append((i, j))

    width = len(s[0])
    height = len(s)

    cheats = find_cheats(roads, start, end, 2)
    count = 0
    for c in cheats:
        if c >= 100:
            count += cheats[c]

    print(count)

    cheats = find_cheats(roads, start, end, 20)
    count = 0
    for c in cheats:
        if c >= 100:
            count += cheats[c]

    print(count)

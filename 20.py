import argparse
import math

#function Dijkstra(Graph, source):
#
#    for each vertex v in Graph.Vertices:
#        dist[v] ← INFINITY
#        prev[v] ← UNDEFINED
#        add v to Q
#    dist[source] ← 0
#
#    while Q is not empty:
#        u ← vertex in Q with minimum dist[u]
#        remove u from Q
#
#        for each neighbor v of u still in Q:
#            alt ← dist[u] + Graph.Edges(u, v)
#            if alt < dist[v]:
#                dist[v] ← alt
#                prev[v] ← u
#
#    return dist[], prev[]

def cheat(pos, roads, walls, count, visited):
    for dy in [-1, 0, 1]:
        for dx in [-1, 0, 1]:

def dijkstra(g, s):
    dist = {}
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

    return dist

if __name__ == '__main__':
    arg_parser = argparse.ArgumentParser()
    arg_parser.add_argument('file')
    args = arg_parser.parse_args()

    s = ""
    with open(args.file) as file:
        s = file.read()
    s = s.split('\n')

    walls = []
    roads = []
    start = None
    end = None

    for i in range(0, len(s)):
        for j in range(0, len(s[0])):
            if s[i][j] == '#':
                walls.append((i, j))
            elif s[i][j] == '.':
                roads.append((i, j))
            elif s[i][j] == 'S':
                start = (i, j)
                roads.append((i, j))
            elif s[i][j] == 'E':
                end = (i, j)
                roads.append((i, j))

    width = len(s[0])
    height = len(s)

    dist_start = dijkstra(roads, start)
    dist_end = dijkstra(roads, end)

    base = dist_start[end]
    count = {}
    for i in range(0, len(s)):
        for j in range(0, len(s[0])):
            if (i, j) not in roads:
                continue

            for dy in [-1, 0, 1]:
                for dx in [-1, 0, 1]:
                    if dy and dx:
                        continue
                    if not dy and not dx:
                        continue

                    if (i + dy, j + dx) not in walls:
                        continue

                    for dy2 in [-1, 0, 1]:
                        for dx2 in [-1, 0, 1]:
                            if dy2 and dx2:
                                continue
                            if not dy2 and not dx2:
                                continue
                            if (i + dy + dy2, j + dx + dx2) == (i, j):
                                continue

                            if (i + dy + dy2, j + dx + dx2) not in roads:
                                continue

                            delta = base - (dist_start[(i, j)] + dist_end[(i + dy + dy2, j + dx + dx2)] + 2)
                            if delta < 0:
                                continue

                            if delta in count:
                                count[delta] += 1
                            else:
                                count[delta] = 1

    a = 0
    for c in count:
        if c >= 100:
            a += count[c]

    print(a)
 #    for i in range(0, len(s) - 1):
 #       for j in range(0, len(s[0])):
 #           cheat1 = (i, j)
 #           cheat2 = (i + 1, j)
 #           if cheat1 not in walls:
 #               cheat1 = None
 #           if cheat2 not in walls:
 #               cheat2 = None
 #
 #           if not cheat1 and not cheat2:
 #               continue
 #
 #           if (cheat1, cheat2) in cheats or (cheat2, cheat1) in cheats:
 #               continue
 #
 #           cheats[(cheat1, cheat2)] = True
 #
 #           roads2 = roads.copy()
 #           if cheat1:
 #               roads2.append(cheat1)
 #           if cheat2:
 #               roads2.append(cheat2)
 #
 #           d = dijkstra(roads2, start)
 #           if (no_cheat_time - d[end]) in count:
 #               count[no_cheat_time - d[end]] += 1
 #           else:
 #               count[no_cheat_time - d[end]] = 1
 #
 #           if no_cheat_time - d[end] == 64:
 #               print(cheat1, cheat2)


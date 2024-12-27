import argparse

if __name__ == '__main__':
    arg_parser = argparse.ArgumentParser()
    arg_parser.add_argument('file')
    args = arg_parser.parse_args()

    s = ""
    with open(args.file) as file:
        s = file.read()

    s = s.split('\n')
    for i in range(0, len(s)):
        s[i] = s[i].split('-')

    V = []
    neighbours = {}
    for pair in s:
        if pair[0] in neighbours:
            neighbours[pair[0]].append(pair[1])
        else:
            neighbours[pair[0]] = [pair[1]]

        if pair[1] in neighbours:
            neighbours[pair[1]].append(pair[0])
        else:
            neighbours[pair[1]] = [pair[0]]

        if pair[0] not in V:
            V.append(pair[0])
        if pair[1] not in V:
            V.append(pair[1])

    sccs = []
    for v in V:
        for w in neighbours[v]:
            for x in neighbours[w]:
                for y in neighbours[x]:
                    if y == v:
                        scc = set()
                        scc.add(v)
                        scc.add(w)
                        scc.add(x)
    
                        if scc and scc not in sccs:
                            sccs.append(scc)
    
    count = 0
    for scc in sccs:
        for node in scc:
            if node[0] == 't':
                count += 1
                break
    
    print(count)

    cliques = []
    for v in V:
        a = set()
        a.add(v)
        for w in V:
            b = True
            for u in a:
                if u not in neighbours[w]:
                    b = False
                    break
            if b:
                a.add(w)

        cliques.append(a)

    largest = set()
    for clique in cliques:
        if len(clique) > len(largest):
            largest = clique

    largest = list(largest)
    largest.sort()
    for i in range(0, len(largest)):
        print(largest[i], end='')

        if i != len(largest) - 1:
            print(',', end='')

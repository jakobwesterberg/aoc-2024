import argparse

if __name__ == '__main__':
    arg_parser = argparse.ArgumentParser()
    arg_parser.add_argument('file')
    args = arg_parser.parse_args()

    with open(args.file) as file:
        s = file.read()
        s = s.split('\n')
        
        antennas = {}
        for y in range(0, len(s)):
            for x in range(0, len(s[0])):
                c = s[y][x]

                if c.isalnum():
                    if c in antennas:
                        antennas[c].append((x, y))
                    else:
                        antennas[c] = [(x, y)]

        nodes = []
        more_nodes = []
        for a in antennas:
            a = antennas[a]
            for i in range(0, len(a)):
                for j in range(0, len(a)):
                    if i == j:
                        continue

                    delta_x = a[j][0] - a[i][0]
                    delta_y = a[j][1] - a[i][1]
                    node = (a[i][0] - delta_x, a[i][1] - delta_y)

                    if node[0] >= 0 and node[0] < len(s[0]) and node[1] >= 0 \
                       and node[1] < len(s):
                        nodes.append(node)

                    n = 1
                    while True:
                        node2 = (node[0] + n * delta_x, node[1] + n * delta_y)
                        if node2[0] < 0 or node2[0] >= len(s[0]) or node2[1] < 0 \
                           or node2[1] >= len(s):
                            break;
                        else:
                            more_nodes.append(node2)
                            n += 1

                    n = -1
                    while True:
                        node2 = (node[0] - n * delta_x, node[1] - n * delta_y)
                        if node2[0] < 0 or node2[0] >= len(s[0]) or node2[1] < 0 \
                           or node2[1] >= len(s):
                            break;
                        else:
                            more_nodes.append(node2)
                            n -= 1

        print(len(set(nodes)))
        print(len(set(more_nodes)))

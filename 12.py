import argparse

def search(i, j, plant, visited, s, perimiter, area):
    if i < 0 or j < 0 or i >= len(s) or j >= len(s[0]):
        if (i, j) in perimiter:
            perimiter[(i, j)] += 1
        else:
            perimiter[(i, j)] = 1
    elif s[i][j] != plant:
        if (i, j) in perimiter:
            perimiter[(i, j)] += 1
        else:
            perimiter[(i, j)] = 1
    elif (i, j) in visited:
        pass
    else:
        visited[(i, j)] = True
        area[(i, j)] = True
        search(i - 1, j    , plant, visited, s, perimiter, area)
        search(i + 1, j    , plant, visited, s, perimiter, area)
        search(i,     j - 1, plant, visited, s, perimiter, area)
        search(i,     j + 1, plant, visited, s, perimiter, area)

def diagonal_neighbour(x, y, a):
    for i in range(-1, 2):
        for j in range(-1, 2):
            if ((y + i, x + j) in a) \
               and ((y + i, x) not in a) \
               and ((y, x + j) not in a):
                return True

    return False

if __name__ == '__main__':
    arg_parser = argparse.ArgumentParser()
    arg_parser.add_argument('file')
    args = arg_parser.parse_args()

    s = ""
    with open(args.file) as file:
        s = file.read()

    s = s.split('\n')

    count = 0
    count2 = 0
    visited = {}
    for i in range(0, len(s)):
        for j in range(0, len(s[0])):
            perimiter = {}
            area = {}
            search(i, j, s[i][j], visited, s, perimiter, area)
            count += sum(perimiter.values()) * len(area)

            a = {}
            corners = 0
            for p in area:
                y, x = p

                for dy in [-0.5, 0.5]:
                    for dx in [-0.5, 0.5]:
                        if (x + dx, y + dy) in a:
                            a[(x + dx, y + dy)] += 1
                        else:
                            a[(x + dx, y + dy)] = 1

                if diagonal_neighbour(x, y, area):
                    corners += 1

            for k in a:
                if a[k] == 1:
                    corners += 1
                elif a[k] == 3:
                    corners += 1

            count2 += corners * len(area)

    print(count)
    print(count2)


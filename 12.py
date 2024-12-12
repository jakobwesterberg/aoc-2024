import argparse

def search(i, j, plant, visited, s):
    if i < 0 or j < 0 or i >= len(s) or j >= len(s):
        return (1, 0)
    elif s[i][j] != plant:
        return (1, 0)
    elif (i, j) in visited:
        return (0, 0)
    else:
        visited[(i, j)] = True
        perimiter = 0
        area = 1
        a = search(i - 1, j    , plant, visited, s)
        perimiter += a[0]
        area += a[1]
        a = search(i + 1, j    , plant, visited, s)
        perimiter += a[0]
        area += a[1]
        a = search(i,     j - 1, plant, visited, s)
        perimiter += a[0]
        area += a[1]
        a = search(i,     j + 1, plant, visited, s)
        perimiter += a[0]
        area += a[1]

        return (perimiter, area)

def search2(i, j, plant, visited, s, perimiter):
    if i < 0 or j < 0 or i >= len(s) or j >= len(s):
        if (i, j) in perimiter:
            perimiter[(i, j)] += 1
        else:
            perimiter[(i, j)] = 1
        return ([(i, j)], 0)
    elif s[i][j] != plant:
        if (i, j) in perimiter:
            perimiter[(i, j)] += 1
        else:
            perimiter[(i, j)] = 1
        return ([(i, j)], 0)
    elif (i, j) in visited:
        return ([], 0)
    else:
        visited[(i, j)] = True
        area = 1
        a = search2(i - 1, j    , plant, visited, s, perimiter)
        area += a[1]
        a = search2(i + 1, j    , plant, visited, s, perimiter)
        area += a[1]
        a = search2(i,     j - 1, plant, visited, s, perimiter)
        area += a[1]
        a = search2(i,     j + 1, plant, visited, s, perimiter)
        area += a[1]

        return (perimiter, area)

def asdflkj(x, y, dx, dy, perimiter):
    if len(perimiter) == 0:
        return False

    if not (x, y) in perimiter:
        return False

    del perimiter[(x, y)]

    asdflkj(x + dx, y + dy, dx, dy, perimiter)

    return True

def walk(x, y, dir, sides, perimiter):
    sides += 1
    del perimiter[(x, y)]

    if (x + 1, y) in perimiter:
        sides += walk(x + 1, y, sides, perimiter)
    elif (x, y + 1) in perimiter:
        sides += walk(x, y + 1, sides, perimiter)
    else:
        return sides

if __name__ == '__main__':
    arg_parser = argparse.ArgumentParser()
    arg_parser.add_argument('file')
    args = arg_parser.parse_args()

    s = ""
    with open(args.file) as file:
        s = file.read()

    s = s.split('\n')

    count = 0
    visited = {}
    for i in range(0, len(s)):
        for j in range(0, len(s[0])):
            perimiter = {}
            _, area = search2(i, j, s[i][j], visited, s, perimiter)
            #count += sum(perimiter.values()) * area
            sides = 0
            perimiter_x = perimiter.copy()
            perimiter_y = perimiter.copy()

            while len(perimiter) != 0:
                x, y = next(iter(perimiter))
                walk(x, y, 0, perimiter)

            if sides != 0:
                print(s[i][j])
                print(sides)
            #while len(perimiter_y) != 0:
            #    x, y = next(iter(perimiter_y))
            #    asdflkj(x, y, 0, 1, perimiter_y)
            #    sides += 1

            count += sides * area

    print(count)

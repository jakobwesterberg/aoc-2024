import argparse

def compute_next(xs):
    i = 0
    while i < len(xs):
        s = str(xs[i])
        l = len(s)
        if xs[i] == 0:
            xs[i] =1
            i += 1
        elif l % 2 == 0:
            xs[i] = int(s[0: int(l / 2)])
            i += 1
            xs.insert(i, int(s[int(l / 2): l]))
            i += 1
        else:
            xs[i] = 2024 * xs[i]
            i += 1

    return xs

def func(xs, depth, max_depth, memory):
    if depth == max_depth:
        return len(xs)

    sum = 0
    for x in xs:
        if not (x, depth) in memory:
            a = compute_next([x])
            memory[(x, depth)] = func(a, depth + 1, max_depth, memory)

        sum += memory[(x, depth)]

    return sum

if __name__ == '__main__':
    arg_parser = argparse.ArgumentParser()
    arg_parser.add_argument('file')
    args = arg_parser.parse_args()

    s = ""
    with open(args.file) as file:
        s = file.read()
        s = s.split(' ')
        s = list(map(int, s))

    print(func(s, 0, 25, {}))
    print(func(s, 0, 75, {}))


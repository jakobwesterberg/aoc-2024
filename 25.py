import argparse

if __name__ == '__main__':
    arg_parser = argparse.ArgumentParser()
    arg_parser.add_argument('file')
    args = arg_parser.parse_args()

    s = ""
    with open(args.file) as file:
        s = file.read()

    s = s.split('\n')
    a = [[]]

    height = 0
    for l in s:
        if not l:
            height = 0
            a.append([])
        else:
            height += 1
            a[len(a) - 1].append(l)

    height -= 2

    keys = []
    locks = []
    for e in a:
        is_lock = True
        for c in e[0]:
            if c != '#':
                is_lock = False
                break

        if is_lock:
            locks.append(e)
        else:
            keys.append(e)

    for i in range(0, len(locks)):
        lock = locks[i]
        heights = []
        for w in range(0, len(lock[0])):
            count = -1
            for h in range(0, len(lock)):
                if lock[h][w] == '#':
                    count += 1
            heights.append(count)

        locks[i] = heights

    for i in range(0, len(keys)):
        key = keys[i]
        heights = []
        for w in range(0, len(key[0])):
            count = -1
            for h in range(0, len(key)):
                if key[h][w] == '#':
                    count += 1
            heights.append(count)

        keys[i] = heights

    count = 0
    for lock in locks:
        for key in keys:
            fit = True
            for i in range(0, len(lock)):
                if lock[i] + key[i] > height:
                    fit = False

            if fit:
                count += 1

    print(count)

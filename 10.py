import argparse

if __name__ == '__main__':
    arg_parser = argparse.ArgumentParser()
    arg_parser.add_argument('file')
    args = arg_parser.parse_args()

    s = ""
    with open(args.file) as file:
        s = file.read()

    files = []
    id = 0
    for i in range(0, len(s)):
        if i % 2 == 0:
            files.append((id, int(s[i])))
            id += 1
        else:
            files.append((-1, int(s[i])))

    n = 0
    m = len(files) - 1
    while n + 1 < m:
        while files[n][0] != -1:
            n += 1
        while files[m][0] == -1:
            m -= 1

        _, space = files[n]
        id, file = files[m]

        if space == 0:
            n += 2
        elif space == file:
            tmp = files[n]
            files[n] = files[m]
            files[m] = tmp
        elif space > file:
            files[n] = (id, file)
            files[m] = (-1, file)
            n += 1
            files.insert(n, (-1, space - file))
        elif space < file:
            files[n] = (id, space)
            files[m] = (id, file - space)

    print(files)

    pos = 0
    sum = 0
    for f in files:
        if f[0] == -1:
            pass
        else:
            for i in range(0, f[1]):
                sum += pos * f[0]
                pos += 1

    print(sum)


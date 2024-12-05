import argparse

def parse_rules(s):
    s = s.split("\n")
    for i in range(0, len(s)):
        s[i] = list(map(int, s[i].split('|')))

    a = {}
    for x in s:
        if x[1] in a:
            a[x[1]] = a[x[1]] + [x[0]]
        else:
            a[x[1]] = [x[0]]

    b = {}
    for x in s:
        if x[0] in b:
            b[x[0]] = b[x[0]] + [x[1]]
        else:
            b[x[0]] = [x[1]]

    return a, b

if __name__ == '__main__':
    arg_parser = argparse.ArgumentParser()
    arg_parser.add_argument('file')
    args = arg_parser.parse_args()

    with open(args.file) as file:
        s = file.read()
        s = s.split('\n\n')
        a, b = parse_rules(s[0])

        s = s[1].split('\n')
        for i in range(0, len(s)):
            s[i] = list(map(int, s[i].split(',')))

        good = []
        bad = []
        for xs in s:
            correct = True
            for i in range(0, len(xs)):
                if xs[i] in a and i != len(xs) - 1:
                    if bool(set(xs[i + 1:len(xs)]) & set(a[xs[i]])):
                        correct = False

            if correct:
                good.append(xs)
            else:
                bad.append(xs)

        sum = 0
        for g in good:
            sum += g[int(len(g) / 2)]

        print(sum)

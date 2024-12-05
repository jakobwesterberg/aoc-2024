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

    return a

def parse_page_order(s):
    s = s[1].split('\n')
    for i in range(0, len(s)):
        s[i] = list(map(int, s[i].split(',')))

    return s

def find_good_bad_page_orders(a, s):
    good = []
    bad = []
    for xs in s:
        correct = True
        for i in range(0, len(xs)):
            if xs[i] in a and i != len(xs) - 1:
                if bool(set(xs[i + 1:len(xs)]) & set(a[xs[i]])):
                    correct = False
                    break

        if correct:
            good.append(xs)
        else:
            bad.append(xs)

    return good, bad

def correct_bad_page_orders(a, bad):
    corrected = []
    for xs in bad:
        correct = False
        while not correct:
            correct = True
            for i in range(0, len(xs)):
                for j in range(i + 1, len(xs)):
                    if (xs[i] in a) and (xs[j] in a[xs[i]]):
                        tmp = xs[i]
                        xs[i] = xs[j]
                        xs[j] = tmp
                        correct = False
                        break
        corrected.append(xs)

    return corrected

if __name__ == '__main__':
    arg_parser = argparse.ArgumentParser()
    arg_parser.add_argument('file')
    args = arg_parser.parse_args()

    with open(args.file) as file:
        s = file.read()
        s = s.split('\n\n')
        a = parse_rules(s[0])        
        s = parse_page_order(s)

        good, bad = find_good_bad_page_orders(a, s)
        sum = 0
        for g in good:
            sum += g[int(len(g) / 2)]

        print(sum)

        sum = 0
        for c in correct_bad_page_orders(a, bad):
            sum += c[int(len(c) / 2)]

        print(sum)


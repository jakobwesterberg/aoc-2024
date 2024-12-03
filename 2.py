import argparse

def is_safe(xs):
    inc = all(xs[i] < xs[i + 1] for i in range(0, len(xs) - 1))
    dec = all(xs[i] > xs[i + 1] for i in range(0, len(xs) - 1))

    if not (inc or dec):
        return False

    ge_1 = all(abs(xs[i] - xs[i + 1]) >= 1 for i in range(0, len(xs) - 1))
    le_3 = all(abs(xs[i] - xs[i + 1]) <= 3 for i in range(0, len(xs) - 1))
            
    if not (ge_1 and le_3):
        return False

    return True

if __name__ == '__main__':
    arg_parser = argparse.ArgumentParser()
    arg_parser.add_argument('file')
    args = arg_parser.parse_args()

    with open(args.file) as file:
        s = file.read()
        s = s.split('\n')

        xss = []
        for l in s:
            l = l.split(' ')
            l = list(map(int, l))
            xss += [l]

        safe = 0
        for xs in xss:
            if is_safe(xs):
                safe += 1

        print(safe)

        safe = 0
        for xs in xss:
            if is_safe(xs):
                safe += 1
                continue

            for j in range(0, len(xs)):
                xs_copy = xs.copy()
                del xs_copy[j]
                if is_safe(xs_copy):
                    safe += 1
                    break

        print(safe)


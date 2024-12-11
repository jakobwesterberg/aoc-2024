import argparse

def compute_next(times, xs):
    for _ in range(0, times):
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

if __name__ == '__main__':
    arg_parser = argparse.ArgumentParser()
    arg_parser.add_argument('file')
    args = arg_parser.parse_args()

    s = ""
    with open(args.file) as file:
        s = file.read()
        s = s.split(' ')
        s = list(map(int, s))

def func(xs, depth, memory):
    if depth == 3:
        return len(xs)

    for x in xs:
        if not x in memory:
            a = compute_next(2, [x])
            memory[x] = a

        return func(memory[x], memory)


    memory = {}
    count = 0
    for x in s:
        if not x in memory:
            a = compute_next(2, [x])
            memory[x] = len(a)

            count += 1

            for x2 in a:
                if not x2 in memory:
                    b = compute_next(2, [x2])
                    memory[x2] = len(b)

                count += 1

                for x3 in b:
                    if not x3 in memory:
                        c = compute_next(2, [x3])
                        memory[x3] = len(c)

                    count += memory[x3]

    print(count)

#    s3 = 0
#    for x in s2:
#        if not x in memory:
#            a = compute_next(25, [x])
#            memory[x] = a
#
#        s3 += len(memory[x])
#
#    print(s3)
    #memory = {}
    #for j in range(0, 75):
    #    i = 0
    #    while i < len(s):
    #        string = str(s[i])
    #        length= len(string)
    #
    #        if s[i] in memory:
    #            m = memory[s[i]]
    #            s[i] = m[0]
    #            i += 1
    #            for x in m[1:]:
    #                s.insert(i, x)
    #                i += 1
    #
    #            continue
    #
    #        if s[i] == 0:
    #            new = 1
    #            memory[s[i]] = [new]
    #            s[i] = new
    #            i += 1
    #        elif length % 2 == 0:
    #            new1 = int(string[0: int(length / 2)])
    #            new2 = int(string[int(length / 2): length])
    #            memory[s[i]] = [new1, new2]
    #            s[i] = new1
    #            i += 1
    #            s.insert(i, new2)
    #            i += 1
    #        else:
    #            new = 2024 * s[i]
    #            memory[s[i]] = [new]
    #            s[i] = new
    #            i += 1

#If the stone is engraved with the number 0, it is replaced by a stone engraved with the number 1.
#
#If the stone is engraved with a number that has an even number of digits, it is replaced by two stones. The left half of the digits are engraved on the new left stone, and the right half of the digits are engraved on the new right stone. (The new numbers don't keep extra leading zeroes: 1000 would become stones 10 and 0.)
#
#If none of the other rules apply, the stone is replaced by a new stone; the old stone's number multiplied by 2024 is engraved on the new stone.
#

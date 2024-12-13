import argparse

memory = {}

def cost(a, b, p, score, depth):
    if depth == 100:
        return 0

    if score == p:
        return 0

    score_plus_a = 0

    if (a, depth) in memory:
        score_plus_a = memory(a, depth)
    else:
        score_plus_a = cost(a, b, p, (score[0] + a[0], score[1] + a[1]), depth + 1) + 3

    score_plus_b = 0
    if (b, depth) in memory:
        score_plus_b = memory(b, depth)
    else:
        score_plus_b = cost(a, b, p, (score[0] + b[0], score[1] + b[1]), depth + 1) + 1

    return min(score_plus_a, score_plus_b)

if __name__ == '__main__':
    arg_parser = argparse.ArgumentParser()
    arg_parser.add_argument('file')
    args = arg_parser.parse_args()

    s = ""
    with open(args.file) as file:
        s = file.read()

    s = s.split('\n')
    button_a = []
    button_b = []
    prize = []
    index = 0
    for line in s:
        i = 0
        x = 0
        y = 0
        while i in range(0, len(line)):
            if line[i] == 'X':
                i += 2
                x = ""
                while i < len(line) and line[i].isdigit():
                    x += line[i]
                    i += 1

                x = int(x)
            elif line[i] == 'Y':
                i += 2
                y = ""
                while i < len(line) and line[i].isdigit():
                    y += line[i]
                    i += 1

                y = int(y)
            else:
                i += 1

            if x != 0 and y != 0:
                if index == 0:
                    button_a.append((x, y))
                    index += 1
                elif index == 1:
                    button_b.append((x, y))
                    index += 1
                else:
                    prize.append((x, y))
                    index = 0

                x = 0
                y = 0

    cost = []
    for i in range(0, len(button_a)):
        pos = (0, 0)

        m = 0
        n = 0
        while m != -1:
            while n != -1:

                if m * button_a[i][0] + n * button_b[i][0] > 10000000000000 + prize[i][0] \
                   or m * button_a[i][1] + n * button_b[i][1] > 10000000000000 + prize[i][1]:
                    m = -1
                    n = -1

                if (m * button_a[i][0] + n * button_b[i][0], m * button_a[i][1] + n * button_b[i][1]) \
                   == (10000000000000 + prize[i][0], 10000000000000 + prize[i][1]):
                    cost.append(3 * m + n)
                    m = -1
                    n = -1

                n += 1
            m += 1

    print(sum(cost))

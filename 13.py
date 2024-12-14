import argparse
import numpy as np

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
        for m in range(0, 100):
            for n in range(0, 100):
                if (m * button_a[i][0] + n * button_b[i][0], m * button_a[i][1] + n * button_b[i][1]) \
                   == (prize[i][0], prize[i][1]):
                    cost.append(3 * m + n)
    
    print(sum(cost))

    cost = []
    for i in range(0, len(button_a)):
        prize[i] = (prize[i][0] + 10000000000000, prize[i][1] + 10000000000000)
        a = np.array([[button_a[i][0], button_b[i][0]], [button_a[i][1], button_b[i][1]]])
        b = np.array([prize[i][0], prize[i][1]])
        c = np.linalg.solve(a,b)

        if c[0] < 0 or c[1] < 0:
            continue

        for x in range(-1, 2):
            for y in range(-1, 2):
                if (int(c[0] + x) * button_a[i][0] + int(c[1] + y) * button_b[i][0] == prize[i][0] \
                    and int(c[0] + x) * button_a[i][1] + int(c[1] + y) * button_b[i][1] == prize[i][1]):
                    cost.append(3 * int(c[0] + x) + int(c[1] + y))

    print(sum(cost))

import argparse

def print_positions(p):
    for i in range(0, 103):
        for j in range(0, 101):
            if (j, i) in p:
                print('X', end='')
            else:
                print('.', end='')
        print('')

if __name__ == '__main__':
    arg_parser = argparse.ArgumentParser()
    arg_parser.add_argument('file')
    args = arg_parser.parse_args()

    s = ""
    with open(args.file) as file:
        s = file.read()

    p = []
    v = []

    s = s.split('\n')
    for line in s:
        i = 0
        while i in range(0, len(line)):
            if line[i] == 'p':
                i += 2
                x = ""
                while i < len(line) and (line[i].isdigit() or line[i] == '-'):
                    x += line[i]
                    i += 1

                i += 1
                y = ""
                while i < len(line) and (line[i].isdigit() or line[i] == '-'):
                    y += line[i]
                    i += 1
          
                p.append((int(x), int(y)))

            if line[i] == 'v':
                i += 2
                x = ""
                while i < len(line) and (line[i].isdigit() or line[i] == '-'):
                    x += line[i]
                    i += 1

                i += 1
                y = ""
                while i < len(line) and (line[i].isdigit() or line[i] == '-'):
                    y += line[i]
                    i += 1

                v.append((int(x), int(y)))
            else:
                i += 1

    p_100 = p.copy()
    for j in range(1, 8054):
        for i in range(0, len(p)):
            pos = p[i]
            vel = v[i]
            x = pos[0] + vel[0]
            y = pos[1] + vel[1]

            if x >= 101:
                x = x - 101
            if x < 0:
                x = 101 + x
            if y >= 103:
                y = y - 103
            if y < 0:
                y = 103 + y

            p[i] = (x, y)

        if j == 100:
            p_100 = p.copy()
        if j == 8053:
            print_positions(p)


    q1 = 0
    q2 = 0
    q3 = 0
    q4 = 0
    for r in p_100:
        if r[0] == 50 or r[1] == 51:
            continue

        if r[0] < 50 and r[1] < 51:
            q1 += 1
        elif r[0] < 50 and r[1] > 51:
            q2 += 1
        elif r[0] > 50 and r[1] < 51:
            q3 += 1
        elif r[0] > 50 and r[1] > 51:
            q4 += 1

    print(q1 * q2 * q3 * q4)
    print(8053)


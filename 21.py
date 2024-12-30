import argparse
from functools import lru_cache

# +---+---+---+
# | 7 | 8 | 9 |
# +---+---+---+
# | 4 | 5 | 6 |
# +---+---+---+
# | 1 | 2 | 3 |
# +---+---+---+
#     | 0 | A |
#     +---+---+

number_coordinates = \
    {'7': (0, 0), '8': (0, 1), '9': (0, 2), \
     '4': (1, 0), '5': (1, 1), '6': (1, 2), \
     '1': (2, 0), '2': (2, 1), '3': (2, 2), \
                  '0': (3, 1), 'A': (3, 2) }

#     +---+---+
#     | ^ | A |
# +---+---+---+
# | < | v | > |
# +---+---+---+

arrow_coordinates = \
                {'^': (0, 1), 'A': (0, 2), \
    '<': (1, 0), 'v': (1, 1), '>': (1, 2)}

@lru_cache
def controll_robot2(code, depth, max_depth):
    current = 'A'
    sequence = 0

    if depth == max_depth:
        return len(code)

    g = []
    for k in arrow_coordinates:
        g.append(arrow_coordinates[k])

    for c in code:
        y_current, x_current = arrow_coordinates[current]
        y_c, x_c = arrow_coordinates[c]

        delta_y, delta_x = (y_c - y_current, x_c - x_current)

        seq_y = ''
        if delta_y < 0:
            for i in range(delta_y, 0):
                seq_y += '^'
        elif delta_y > 0:
            for i in range(0, delta_y):
                seq_y += 'v'

        seq_x = ''
        if delta_x < 0:
            for i in range(delta_x, 0):
                seq_x += '<'
        elif delta_x > 0:
            for i in range(0, delta_x):
                seq_x += '>'


        seq1 = seq_y + seq_x + 'A'
        seq2 = seq_x + seq_y + 'A'

        if (y_current + delta_y, x_current) not in g:
            a = controll_robot2(seq2, depth + 1, max_depth)
            sequence += a
        elif (y_current, x_current + delta_x) not in g:
            a = controll_robot2(seq1, depth + 1, max_depth)
            sequence += a
        elif controll_robot2(seq1, depth + 1, max_depth) < controll_robot2(seq2, depth + 1, max_depth):
            a = controll_robot2(seq1, depth + 1, max_depth)
            sequence += a
        else:
            a = controll_robot2(seq2, depth + 1, max_depth)
            sequence += a

        current = c
    
    return sequence

@lru_cache
def controll_robot(code, depth, max_depth):
    current = 'A'
    sequence = 0

    g = []
    for k in number_coordinates:
        g.append(number_coordinates[k])

    for c in code:
        y_current, x_current = number_coordinates[current]
        y_c, x_c = number_coordinates[c]

        delta_y, delta_x = (y_c - y_current, x_c - x_current)

        seq_y = ''
        if delta_y < 0:
            for i in range(delta_y, 0):
                seq_y += '^'
        elif delta_y > 0:
            for i in range(0, delta_y):
                seq_y += 'v'

        seq_x = ''
        if delta_x < 0:
            for i in range(delta_x, 0):
                seq_x += '<'
        elif delta_x > 0:
            for i in range(0, delta_x):
                seq_x += '>'

        seq1 = seq_y + seq_x + 'A'
        seq2 = seq_x + seq_y + 'A'

        if (y_current + delta_y, x_current) not in g:
            a = controll_robot2(seq2, depth + 1, max_depth)
            sequence += a
        elif (y_current, x_current + delta_x) not in g:
            a = controll_robot2(seq1, depth + 1, max_depth)
            sequence += a
        elif controll_robot2(seq1, depth + 1, max_depth) < controll_robot2(seq2, depth + 1, max_depth):
            a = controll_robot2(seq1, depth + 1, max_depth)
            sequence += a
        else:
            a = controll_robot2(seq2, depth + 1, max_depth)
            sequence += a

        current = c
    
    return sequence

if __name__ == '__main__':
    arg_parser = argparse.ArgumentParser()
    arg_parser.add_argument('file')
    args = arg_parser.parse_args()

    s = ""
    with open(args.file) as file:
        s = file.read()

    s = s.split('\n')

    sum_complexity = 0
    for code in s:
        num = int(''.join(str(x) for x in code if x.isdigit()))
        sum_complexity += controll_robot(code, 0, 3) * num

    print(sum_complexity)

    sum_complexity = 0
    for code in s:
        num = int(''.join(str(x) for x in code if x.isdigit()))
        sum_complexity += controll_robot(code, 0, 26) * num

    print(sum_complexity)

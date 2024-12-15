import argparse
import copy

width = 0
height = 0

def print_room(pos, boxes, walls):
    for y in range(0, height):
        for x in range(0, width):
            if (x, y) == pos:
                print('@', end='')
            elif (x, y) in walls:
                print('#', end='')
            elif (x, y) in boxes:
                print('O', end='')
            else:
                print('.', end='')
        print('')

def print_room2(pos, boxes, walls):
    for y in range(0, height):
        for x in range(0, width):
            if (x, y) == pos:
                print('@', end='')
            elif (x, y) in walls:
                print('#', end='')
            else:
                flag = False
                for b in boxes:
                    if (x, y) == b[0]:
                        print('[', end='')
                        flag = True
                        break
                    elif (x, y) == b[1]:
                        print(']', end='')
                        flag = True
                        break

                if not flag:
                    print('.', end='')

        print('')

def move_box(pos, dx, dy, boxes, walls):
    x, y = pos

    if (x + dx, y + dy) in walls:
        return False

    if (x + dx, y + dy) in boxes:
        if move_box((x + dx, y + dy), dx, dy, boxes, walls):
            index = boxes.index(pos)
            boxes[index] = (x + dx, y + dy)
            return True
        else:
            return False

    index = boxes.index(pos)
    boxes[index] = (x + dx, y + dy)

    return True

def make_move(pos, new_pos, boxes, walls):
    if new_pos in walls:
        return pos
    elif new_pos in boxes:
        dx = new_pos[0] - pos[0]
        dy = new_pos[1] - pos[1]

        if move_box(new_pos, dx, dy, boxes, walls):
            return new_pos
        else:
            return pos
    else:
        return new_pos

def move_box2(b, dx, dy, boxes, walls):
    if (b[0][0] + dx, b[0][1] + dy) in walls or (b[1][0] + dx, b[1][1] + dy) in walls:
            return

    for b2 in boxes:
        if b == b2:
            continue

        if (b[0][0] + dx, b[0][1] + dy) == b2[0] or (b[1][0] + dx, b[1][1] + dy) == b2[1] \
           or (b[0][0] + dx, b[0][1] + dy) == b2[1] or (b[1][0] + dx, b[1][1] + dy) == b2[0]:
            move_box2(b2, dx, dy, boxes, walls)

    index = boxes.index(b)
    boxes[index] = [(b[0][0] + dx, b[0][1] + dy), \
                    (b[1][0] + dx, b[1][1] + dy)]

def move_box2_test(b, dx, dy, boxes, walls):
    if (b[0][0] + dx, b[0][1] + dy) in walls or (b[1][0] + dx, b[1][1] + dy) in walls:
            return False

    for b2 in boxes:
        if b == b2:
            continue

        if (b[0][0] + dx, b[0][1] + dy) == b2[0] or (b[1][0] + dx, b[1][1] + dy) == b2[1] \
           or (b[0][0] + dx, b[0][1] + dy) == b2[1] or (b[1][0] + dx, b[1][1] + dy) == b2[0]:
            if not move_box2_test(b2, dx, dy, boxes, walls):
                return False

    return True


def make_move2(pos, new_pos, boxes, walls):
    if new_pos in walls:
        return pos

    for b in boxes:
        if new_pos == b[0] or new_pos == b[1]:
            dx = new_pos[0] - pos[0]
            dy = new_pos[1] - pos[1]

            if not move_box2_test(b, dx, dy, boxes, walls):
                return pos

    for b in boxes:
        if new_pos == b[0] or new_pos == b[1]:
            dx = new_pos[0] - pos[0]
            dy = new_pos[1] - pos[1]

            move_box2(b, dx, dy, boxes, walls)

    return new_pos

def gps(boxes):
    count = 0

    for b in boxes:
        x, y = b
        count += x + 100 * y

    return count

def gps2(boxes):
    count = 0

    for b in boxes:
        if b[0][0] < b[1][0]:
            count += b[0][0] + 100 * b[0][1]
        else:
            count += b[1][0] + 100 * b[1][1]

    return count

def part_1(s):
    s = s.copy()
    walls = []
    boxes = []
    start_pos = (0, 0)

    moves = []

    found_empty_line = False
    y = 0
    for y in range(0, len(s)):
        if s[y] == '':
            found_empty_line = True
            height = y
        elif found_empty_line:
            for x in range(0, len(s[y])):
                moves.append(s[y][x])
        else:
            width = len(s[y])
            for x in range(0, len(s[y])):
                if s[y][x] == '#':
                    walls.append((x, y))
                elif s[y][x] == 'O':
                    boxes.append((x, y))
                elif s[y][x] == '@':
                    start_pos = (x, y)


    pos = start_pos
    while moves:
        x, y = pos
        m = moves.pop(0)

        if m == '^':
            pos = make_move(pos, (x, y - 1), boxes, walls)
        elif m == 'v':
            pos = make_move(pos, (x, y + 1), boxes, walls)
        elif m == '>':
            pos = make_move(pos, (x + 1, y), boxes, walls)
        elif m == '<':
            pos = make_move(pos, (x - 1, y), boxes, walls)

    print(gps(boxes))

def part_2(s):
    s = s.copy()
    walls = []
    boxes = []
    start_pos = (0, 0)

    moves = []

    found_empty_line = False
    y = 0

    for y in range(0, len(s)):
        if s[y] == '':
            found_empty_line = True
            height = y
        elif found_empty_line:
            for x in range(0, len(s[y])):
                moves.append(s[y][x])
        else:
            width = len(s[y]) * 2
            for x in range(0, len(s[y])):
                if s[y][x] == '#':
                    walls.append((2 * x, y))
                    walls.append((2 * x + 1, y))
                elif s[y][x] == 'O':
                    boxes.append([(2 * x, y), (2 * x + 1, y)])
                elif s[y][x] == '@':
                    start_pos = (2 * x, y)


    pos = start_pos

    while moves:
        x, y = pos
        m = moves.pop(0)

        if m == '^':
            pos = make_move2(pos, (x, y - 1), boxes, walls)
        elif m == 'v':
            pos = make_move2(pos, (x, y + 1), boxes, walls)
        elif m == '>':
            pos = make_move2(pos, (x + 1, y), boxes, walls)
        elif m == '<':
            pos = make_move2(pos, (x - 1, y), boxes, walls)


    print(gps2(boxes))

if __name__ == '__main__':
    arg_parser = argparse.ArgumentParser()
    arg_parser.add_argument('file')
    args = arg_parser.parse_args()

    s = ""
    with open(args.file) as file:
        s = file.read()

    s = s.split('\n')

    part_1(s)
    part_2(s)


import argparse

def add_mul(s, res, ops):
    if len(ops) == 0:
        return False

    if len(ops) == 1:
        if s + ops[0] == res:
            return True
        if s * ops[0] == res:
            return True

    return add_mul(s + ops[0], res, ops[1:]) \
        or add_mul(s * ops[0], res, ops[1:])

def add_mul_conc(s, res, ops):
    if len(ops) == 0:
        return False

    if len(ops) == 1:
        if s + ops[0] == res:
            return True
        if s * ops[0] == res:
            return True
        if int(str(s) + str(ops[0])) == res:
            return True

    return add_mul_conc(s + ops[0], res, ops[1:]) \
        or add_mul_conc(s * ops[0], res, ops[1:]) \
        or add_mul_conc(int(str(s) + str(ops[0])), res, ops[1:])

if __name__ == '__main__':
    arg_parser = argparse.ArgumentParser()
    arg_parser.add_argument('file')
    args = arg_parser.parse_args()

    with open(args.file) as file:
        s = file.read()
        s = s.split('\n')

        results = []
        operands = []
        for line in s:
            line = line.split(':')
            results.append(int(line[0]))
            line = line[1].split(' ')
            line = [x for x in line if x != '']
            line = list(map(int, line))
            operands.append(line)

        part_one = 0
        part_two = 0
        for i in range(0, len(results)):
            if add_mul(operands[i][0], results[i], operands[i][1:]):
                part_one += results[i]
                part_two += results[i]
            elif add_mul_conc(operands[i][0], results[i], operands[i][1:]):
                part_two += results[i]

        print(part_one)
        print(part_two)


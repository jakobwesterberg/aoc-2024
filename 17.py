import argparse
import math

a = 0
b = 0
c = 0
program = []

def get_number(operand):
    global a
    global b
    global c

    if 0 <= operand and operand <= 3:
        return operand

    if operand == 4:
            return a
    if operand == 5:
            return b
    if operand == 6:
            return c

def run():
    global a
    global b
    global c
    global program

    output = ""
    pc = 0
    while pc < len(program):
        opcode = program[pc]
        operand = program[pc + 1]

        if opcode == 0:
            op1 = a
            op2 = get_number(operand)
            a = int(op1 / (2**op2))
        if opcode == 1:
            op1 = b
            op2 = operand
            b = op1 ^ op2
        if opcode == 2:
            op1 = get_number(operand)
            b = op1 % 8
        if opcode == 3:
            op1 = a
            op2 = operand

            if a:
                pc = operand
                continue
        if opcode == 4:
            op1 = b
            op2 = c
            b = op1 ^ op2
        if opcode == 5:
            op1 = get_number(operand)
            output += str(op1 % 8)
            output += ","
        if opcode == 6:
            op1 = a
            op2 = get_number(operand)
            b = int(op1 / (2**op2))
        if opcode == 7:
            op1 = a
            op2 = get_number(operand)
            c = int(op1 / (2**op2))

        pc += 2

    output = output[0:len(output) - 1]
    return output

def find(index, k, candidates):
    global a
    global b
    global c
    global program

    for i in range(0, 7):
        k[index] = i
        a = 0
        for j in range(0, len(k)):
            a += 8**j * k[j]

        candidates.append((index, a))
        output = run()
        output = list(map(int, output.split(',')))

        a = 0
        b = 0
        c = 0

        if len(output) == len(program) and output[index] == program[index]:
            if index != 0 and find(index - 1, k, candidates):
                return True
            elif index == 0:
                return True

    return False

if __name__ == '__main__':
    arg_parser = argparse.ArgumentParser()
    arg_parser.add_argument('file')
    args = arg_parser.parse_args()

    s = ""
    with open(args.file) as file:
        s = file.read()

    s = s.split('\n')

    found_empty_line = False
    for line in s:
        if line == "":
            found_empty_line = True
        elif not found_empty_line:
            i = 0
            while i < len(line):
                r = ""
                if line[i] == 'A':
                    i += 3
                    while i < len(line) and line[i].isdigit():
                        r += line[i]
                        i += 1
                    a = int(r)
                elif line[i] == 'B':
                    i += 3
                    while i < len(line) and line[i].isdigit():
                        r += line[i]
                        i += 1
                    b = int(r)
                elif line[i] == 'C':
                    i += 3
                    while i < len(line) and line[i].isdigit():
                        r += line[i]
                        i += 1
                    c = int(r)
                else:
                    i += 1
        else:
            i = 0
            while i < len(line):
                if line[i] == 'm':
                    i += 3
                    while i < len(line):
                        op = line[i]
                        i += 2
                        program.append(int(op))
                else:
                    i += 1

    output = run()
    print(output)

    k = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    candidates = []
    find(15, k, candidates)

    best_candidate = (15, math.inf)
    for candidate in candidates:
        if candidate[0] <= best_candidate[0]:
            if candidate[0] != best_candidate[0]:
                best_candidate = candidate
            elif candidate[1] < best_candidate[1]:
                best_candidate = candidate

    a_inital = best_candidate[1]
    b_inital = b
    c_inital = c

    for i in range(0, 10000):
        a = a_inital + i
        b = b_inital
        c = c_inital
        output = run()
        output = list(map(int, output.split(',')))
        if output == program:
            print(a_inital + i)
            break

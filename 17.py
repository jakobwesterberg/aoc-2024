import argparse

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

def score(output, program):
    s = 0
    for i in range(0, len(output)):
            if output[i] == program[i]:
                s += 1
    return s

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

    #output = run()
    #output = list(map(int, output.split(',')))

    #a_inital = 181484988207182

    #for i in range(0, 15):
    #    for j in range(0, 9)
    #a_test = "00000000000000"



    #a_inital = 8**0*1 + 8**1*1 + 8**2*1 + 8**3*2 + 8**4*3 + 8**5*2 \
    #    + 8**6*0 + 8**7*6 + 8**8*6 + 8**9*9 + 8**10*1 + 8**11*7  + 8**12*1 + 8**13*1 + 8**14*1 + 8**15*6
    #print(a_inital)
    #a_inital = 216185278996041
    #a_inital = 0
    b_inital = b
    c_inital = c

    output = []
    #while output != program:

    a_inital = 8**0*4 + 8**1*4 + 8**2*4 + 8**3*2 + 8**4*3 + 8**5*2 \
        + 8**6*0 + 8**7*6 + 8**8*6 + 8**9*9 + 8**10*1 + 8**11*7  + 8**12*1 + 8**13*1 + 8**14*1 + 8**15*6
    a = a_inital
    print(program)
    for i in range(0, 1):
        a = a_inital + i
        b = b_inital
        c = c_inital
        output = run()
        output = list(map(int, output.split(',')))
        print(output)

        #if len(output) != len(program):
        #     pass
        #else:
        #     print(score(output, program))

#[6] 0
#[7] 1
#[5] 2
#[6] 3
#[2] 4
#[3] 5
#[0] 6
#[1] 7
# 8**0*1 + 8**1*1 + 8**2*1 + 8**3*1 + 8**4*1 + 8**5*1 + 8**6*1 + 8**7*1 + 8**8*1 + 8**9*1 + 8**10*1 + 8**11*1  + 8**12*1 + 8**13*1 + 8**14*1 + 8**15*1
# 2,       4,       1,       3,       7,       5,       0,       3,       4,       3,        1,        5,        5,        5,        3, 0


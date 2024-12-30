import argparse
import copy

def all_z_have_values(wires):
    for wire in wires:
        if wire[0] == 'z' and wires[wire] == None:
            return False

    return True

def calculate_output(wires):
    zs = []
    for wire in wires:
        if wire[0] == 'z':
            zs.append(wire)
                    
    zs.sort(reverse=True)
                    
    binary = ''
    for z in zs:
        binary += str(wires[z])
                    
    return int(binary, 2)

if __name__ == '__main__':
    arg_parser = argparse.ArgumentParser()
    arg_parser.add_argument('file')
    args = arg_parser.parse_args()

    s = ""
    with open(args.file) as file:
        s = file.read()

    s = s.split('\n')

    wires = {}
    gates = []

    first_half = True
    for line in s:
        if line == '':
            first_half = False
            continue

        if first_half:
            line = line.split(': ')
            wires[line[0]] = int(line[1])
        else:
            line = line.split(' -> ')
            line[0] = line[0].split(' ')

            input1 = line[0][0]
            gate = line[0][1]
            input2 = line[0][2]
            output = line[1]

            gates.append([gate, input1, input2, output])
            if input1 not in wires:
                wires[input1] = None
            if input2 not in wires:
                wires[input2] = None
            if output not in wires:
                wires[output] = None

    gates_start = copy.deepcopy(gates)
    wires_start = copy.deepcopy(wires)

    xs = []
    for wire in wires:
        if wire[0] == 'x':
            xs.append(wire)

    xs.sort(reverse=True)

    x_binary = ''
    for x in xs:
        x_binary += str(wires[x])

    ys = []
    for wire in wires:
        if wire[0] == 'y':
            ys.append(wire)

    ys.sort(reverse=True)

    y_binary = ''
    for y in ys:
        y_binary += str(wires[y])

    while not all_z_have_values(wires):
        for gate in gates:
            gate_type = gate[0]
            input1 = gate[1]
            input2 = gate[2]
            output = gate[3]

            if wires[input1] == None or wires[input2] == None:
                continue

            if gate_type == 'AND':
                wires[output] = wires[input1] & wires[input2]
            elif gate_type == 'OR':
                wires[output] = wires[input1] | wires[input2]
            elif gate_type == 'XOR':
                wires[output] = wires[input1] ^ wires[input2]

    print(calculate_output(wires))

    sum_x_y = int(x_binary, 2) + int(y_binary, 2)


    print('gbs,hwq,thm,wrm,wss,z08,z22,z29') # Found through a lot of manual labour

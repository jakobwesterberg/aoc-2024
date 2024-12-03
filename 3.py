import argparse

def eat_number(i, s):
    if i >= len(s):
        raise Exception()

    if not s[i].isdigit():
        raise Exception()

    num = ""
    j = 0
    while (i < len(s) and s[i].isdigit() and j < 3):
        num += s[i]
        i += 1
        j += 1

    return num, i

def eat_char(c, i, s):
    if i >= len(s):
        raise Exception()

    if c != s[i]:
        raise Exception()

    i += 1
    return i

def parse(s, do=None, dont=None):
    res = 0
    i = 0

    enabled = True
    while(i < len(s)):
        if do and dont:
            if i in do:
                enabled = True
            elif i in dont:
                enabled = False
        try:
            i = eat_char('m', i, s)
            i = eat_char('u', i, s)
            i = eat_char('l', i, s)
            i = eat_char('(', i, s)
            n1, i = eat_number(i, s)
            i = eat_char(',', i, s)
            n2, i = eat_number(i, s)
            i = eat_char(')', i, s)

            if enabled:
                res += int(n1) * int(n2)
        except Exception as e:
            i += 1
            continue

    print(res)

def find_substrings(sub, s):
    res = []
    i = 0
    while i < len(s):
        i = s.find(sub, i)

        if i == -1:
            break

        res.append(i)
        i += 1

    return res

if __name__ == '__main__':
    arg_parser = argparse.ArgumentParser()
    arg_parser.add_argument('file')
    args = arg_parser.parse_args()

    with open(args.file) as file:
        s = file.read()

        parse(s)

        do = find_substrings("do()", s)
        dont = find_substrings("don't()", s)
        parse(s, do, dont)


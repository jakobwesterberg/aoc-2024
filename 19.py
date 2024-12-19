import argparse

def test_pattern(towels, pattern, m):
    if pattern == '':
        m[pattern] = 1
        return True

    if pattern in m:
        return m[pattern] > 0

    m[pattern] = 0

    for i in range(1, len(pattern) + 1):
        if pattern[0:i] not in towels:
            continue

        if test_pattern(towels, pattern[i:], m):
            m[pattern] += m[pattern[i:]]

    return m[pattern] > 0

if __name__ == '__main__':
    arg_parser = argparse.ArgumentParser()
    arg_parser.add_argument('file')
    args = arg_parser.parse_args()

    s = ""
    with open(args.file) as file:
        s = file.read()

    s = s.split('\n')
    towels = s[0].split(', ')
    patterns = s[2:]

    memory = {}
    works = 0
    arrangements = 0
    for pattern in patterns:
        if (test_pattern(towels, pattern, memory)):
            works += 1

        arrangements += memory[pattern]

    print(works)
    print(arrangements)

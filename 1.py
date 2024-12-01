import argparse

if __name__ == '__main__':
    arg_parser = argparse.ArgumentParser()
    arg_parser.add_argument('file')
    args = arg_parser.parse_args()

    with open(args.file) as file:
        s = file.read()
        s = s.replace('   ', '\n')
        s = s.split('\n')
        s = list(map(int, s))

        l1 = []
        l2 = []
        i = 0
        while i < len(s):
            l1.append(s[i])
            i += 1
            l2.append(s[i])
            i += 1
            
        l1.sort()
        l2.sort()

        d = 0
        for i in range(0, len(l1)):
            d += abs(l1[i] - l2[i])

        print(d)

        similarity = 0
        for i in range(0, len(l1)):
            similarity += l1[i] * l2.count(l1[i])

        print(similarity)

import argparse

def next_number(n1):
    n2 = n1
    n2 ^= n1 * 64
    n2 = n2 % 16777216

    tmp = n2 / 32
    tmp = int(tmp)
    n2 ^= tmp
    n2 = n2 % 16777216

    tmp = n2 * 2048
    n2 ^= tmp
    n2 = n2 % 16777216

    return n2

def price(num):
    return num % 10

if __name__ == '__main__':
    arg_parser = argparse.ArgumentParser()
    arg_parser.add_argument('file')
    args = arg_parser.parse_args()

    s = ""
    with open(args.file) as file:
        s = file.read()

    s = s.split('\n')
    s = list(map(int, s))

    x = 0
    for n in s:
        next = n
        for i in range(0, 2000):
            next = next_number(next)
    
        x += next
    
    print(x)

    ps = []
    dps = []

    for n in s:
        next = n
        p = []
        for i in range(0, 2000):
            p.append(price(next))
            next = next_number(next)

        dp = []
        for i in range(0, len(p) - 1):
            dp.append(p[i + 1] - p[i])


        ps.append(p)
        dps.append(dp)

    sequence = []
    best_price = 0

    for a in range(-9, 10):
        for b in range(-9, 10):
            for c in range(-9, 10):
                for d in range(-9, 10):
    
                    sequence = [a, b, c, d]
                    current_price = 0

                    change = sum(sequence)
                    if change < 0:
                        continue
    
                    if change > 9:
                        continue

                    for j in range(0, len(dps)):
    
                        dp = dps[j]
                        p = ps[j]
    
                        for i in range(0, len(dp) - 4):
                            if change + p[i + 1] > 9:
                                continue
                            if dp[i:i + 4] == sequence:
                                current_price += p[i + 4]
                                break

                    if current_price > best_price:
                        best_price = current_price

    print(best_price)

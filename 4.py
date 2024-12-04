import argparse

def search_n(s, i, j):
    if i < 3:
        return False

    return  s[i - 1][j] == "M" \
        and s[i - 2][j] == "A" \
        and s[i - 3][j] == "S"

def search_s(s, i, j):
    if len(s) - 4 < i:
        return False

    return  s[i + 1][j] == "M" \
        and s[i + 2][j] == "A" \
        and s[i + 3][j] == "S"

def search_e(s, i, j):
    if len(s[i]) - 4 < j:
        return False

    return  s[i][j + 1] == "M" \
        and s[i][j + 2] == "A" \
        and s[i][j + 3] == "S"

def search_w(s, i, j):
    if j < 3:
        return False

    return  s[i][j - 1] == "M" \
        and s[i][j - 2] == "A" \
        and s[i][j - 3] == "S"

def search_ne(s, i, j):
    if (i < 3 or len(s[i]) - 4 < j):
        return False

    return  s[i - 1][j + 1] == "M" \
        and s[i - 2][j + 2] == "A" \
        and s[i - 3][j + 3] == "S"

def search_se(s, i, j):
    if (len(s) - 4 < i or len(s[i]) - 4 < j):
        return False

    return  s[i + 1][j + 1] == "M" \
        and s[i + 2][j + 2] == "A" \
        and s[i + 3][j + 3] == "S"

def search_sw(s, i, j):
    if (len(s) - 4 < i or j < 3):
        return False

    return  s[i + 1][j - 1] == "M" \
        and s[i + 2][j - 2] == "A" \
        and s[i + 3][j - 3] == "S"

def search_nw(s, i, j):
    if (i < 3 or j < 3):
        return False

    return  s[i - 1][j - 1] == "M" \
        and s[i - 2][j - 2] == "A" \
        and s[i - 3][j - 3] == "S"

def search_mas(s, i, j):
    if (i < 1 or j < 1):
        return False

    if (len(s) - 2 < i or len(s[i]) - 2 < j):
        return False

    nw_to_se = s[i - 1][j - 1] == "M" and s[i + 1][j + 1] == "S"
    se_to_nw = s[i - 1][j - 1] == "S" and s[i + 1][j + 1] == "M"

    ne_to_sw = s[i - 1][j + 1] == "M" and s[i + 1][j - 1] == "S"
    sw_to_ne = s[i - 1][j + 1] == "S" and s[i + 1][j - 1] == "M"

    return ((nw_to_se or se_to_nw) and (ne_to_sw or sw_to_ne))

if __name__ == '__main__':
    arg_parser = argparse.ArgumentParser()
    arg_parser.add_argument('file')
    args = arg_parser.parse_args()

    with open(args.file) as file:
        s = file.read()
        s = s.split()

        count = 0
        for i in range(0, len(s)):
            for j in range(0, len(s[0])):
                if (s[i][j] != 'X'):
                    continue

                if search_n(s, i, j):
                    count += 1
                if search_s(s, i, j):
                    count += 1
                if search_e(s, i, j):
                    count += 1
                if search_w(s, i, j):
                    count += 1
                if search_ne(s, i, j):
                    count += 1
                if search_se(s, i, j):
                    count += 1
                if search_sw(s, i, j):
                    count += 1
                if search_nw(s, i, j):
                    count += 1

        print(count)
        count = 0

        for i in range(0, len(s)):
            for j in range(0, len(s[0])):
                if (s[i][j] != 'A'):
                    continue

                if search_mas(s, i, j):
                    count += 1

        print(count)


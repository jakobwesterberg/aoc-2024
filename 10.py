import argparse

def dfs_helper(c, i, j, visited, s):
    if i < 0 or i == len(s) or j < 0 or j == len(s[0]):
        return 0

    if s[i][j] != c:
        return 0

    if (i, j) in visited:
        return 0

    visited[(i, j)] = True

    if s[i][j] == 9:
        return 1

    return dfs_helper(c + 1, i - 1, j    , visited, s) \
         + dfs_helper(c + 1, i + 1, j    , visited, s) \
         + dfs_helper(c + 1, i    , j - 1, visited, s) \
         + dfs_helper(c + 1, i    , j + 1, visited, s)

def dfs(i, j, s):
    return dfs_helper(0, i, j, {}, s)


def search_helper(c, i, j, visited, s):
    if i < 0 or i == len(s) or j < 0 or j == len(s[0]):
        return 0

    if s[i][j] != c:
        return 0

    if (i, j) in visited:
        return 0

    visited[(i, j)] = True

    if s[i][j] == 9:
        return 1

    return search_helper(c + 1, i - 1, j    , visited.copy(), s) \
         + search_helper(c + 1, i + 1, j    , visited.copy(), s) \
         + search_helper(c + 1, i    , j - 1, visited.copy(), s) \
         + search_helper(c + 1, i    , j + 1, visited.copy(), s)

def search(i, j, s):
    return search_helper(0, i, j, {}, s)

if __name__ == '__main__':
    arg_parser = argparse.ArgumentParser()
    arg_parser.add_argument('file')
    args = arg_parser.parse_args()

    s = ""
    with open(args.file) as file:
        s = file.read()

    s = s.split('\n')
    for i in range(0, len(s)):
        s[i] = list(map(int, s[i]))

    score = 0
    score2 = 0
    for i in range(0, len(s)):
        for j in range(0, len(s[0])):
            if s[i][j] != 0:
                continue

            score += dfs(i, j, s)
            score2 += search(i, j, s)

    print(score)
    print(score2)

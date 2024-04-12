def dfs(forest, i, j, n):
    if i < 0 or i >= n or j < 0 or j >= 3 or forest[i][j] == 'W':
        return 0
    if forest[i][j] == 'C':
        return 1
    forest[i][j] = 'W'
    mushrooms = 0
    for di in range(-1, 2):
        mushrooms += dfs(forest, i + 1, j + di, n)
    return mushrooms

def max_white_mushrooms(n, forest):
    max_mushrooms = 0
    for j in range(3):
        max_mushrooms = max(max_mushrooms, dfs(forest, 0, j, n))
    return max_mushrooms

n = int(input())
forest = [list(input()) for _ in range(n)]

print(max_white_mushrooms(n, forest))

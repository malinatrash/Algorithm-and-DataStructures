def solve(m):
    res = list(zip(*m[::-1]))
    return res


n, m = map(int, input().split())
matrix = [list(map(int, input().split())) for _ in range(n)]

res = solve(matrix)

for i in res:
    print(*i)

def solve(m) -> int:
    max5 = -1
    for i in range(len(m) - 6):
        cur_list = m[i:i+7]
        if 3 not in cur_list and 2 not in cur_list:
            cur_max = 0
            for z in cur_list:
                if z == 5:
                    cur_max += 1
            max5 = max(max5, cur_max)
    return max5


n = int(input())
m = list(map(int, input().split()))

print(solve(m))

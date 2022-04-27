def DFS(num, cnt):
    global b, min_cnt
    if num == b and min_cnt > cnt:
        min_cnt = cnt
        return

    for i in [num * 2, num * 10 + 1]:
        if i <= b:
            DFS(i, cnt+1)

a, b = map(int, input().split())
min_cnt = float('inf')

DFS(a, 0)

result = 0
if min_cnt == float('inf'):
    result = -1
else:
    result = min_cnt + 1
print(result)
from collections import deque

def BFS(args, T):
    q = deque()
    for arg in args:
        q.append(arg)
    while T:
        for _ in range(len(q)):
            val, i, j = q.popleft()
            for k in range(4):
                ni = i + di[k]
                nj = j + dj[k]
                if 0 <= ni < n and 0 <= nj < n and not matrix[ni][nj]:
                    q.append([val, ni, nj])
                    matrix[ni][nj] = val
        T -= 1
di = [0, 0, -1, 1]
dj = [1, -1, 0, 0]
n, k = map(int , input().split())
matrix = [list(map(int, input().split())) for _ in range(n)]
s, x, y = map(int, input().split())

point = []
for i in range(n):
    for j in range(n):
        if matrix[i][j]:
            point.append([matrix[i][j], i, j])

point.sort()

BFS(point, s)

print(matrix[x-1][y-1])
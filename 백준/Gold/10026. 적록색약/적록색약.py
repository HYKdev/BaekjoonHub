# 적록색약

from collections import deque

di = [0, 0, -1, 1]
dj = [1, -1, 0, 0]
def BFS(x, y):
    visited[x][y] = 1
    q.append([x, y])
    while q:
        i, j = q.pop()
        for k in range(4):
            ni = i + di[k]
            nj = j + dj[k]
            if 0 <= ni < n and 0 <= nj < n and not visited[ni][nj]:
                if matrix[ni][nj] == matrix[i][j]:
                    visited[ni][nj] = 1
                    q.append([ni,nj])

n = int(input())

matrix = [list(input()) for _ in range(n)]
visited = [[0 for _ in range(n)] for _ in range(n)]
cnt_RGB = 0
cnt_RB = 0

q = deque()
for i in range(n):
    for j in range(n):
        if not visited[i][j]:
            BFS(i, j)
            cnt_RGB += 1

for i in range(n):
    for j in range(n):
        if matrix[i][j] == 'G':
            matrix[i][j] = 'R'

visited = [[0 for _ in range(n)] for _ in range(n)]

for i in range(n):
    for j in range(n):
        if not visited[i][j]:
            BFS(i, j)
            cnt_RB += 1
print(cnt_RGB, cnt_RB)
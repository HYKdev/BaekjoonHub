import sys
input = sys.stdin.readline

from collections import deque
from itertools import combinations

di = [0, 0, -1, 1]
dj = [1, -1, 0, 0]

def BFS(arr):
    q = deque()
    for ar in arr:
        q.append(ar)
        visited[ar[0]][ar[1]] = 1
    while q:
        i, j = q.popleft()
        for k in range(4):
            ni = i + di[k]
            nj = j + dj[k]
            if 0 <= ni < n and 0 <= nj < n:
                if not visited[ni][nj] and matrix[ni][nj] != 1:
                    visited[ni][nj] = visited[i][j] + 1
                    q.append([ni, nj])

def virus_check():
    for i in range(n):
        for j in range(n):
            if not visited[i][j] and matrix[i][j] == 0:
                ans_list.append(-1)
                return

    time = 1
    for i in range(n):
        for j in range(n):
            if visited[i][j] and matrix[i][j] == 0 and time < visited[i][j]:
                time = visited[i][j]
    ans_list.append(time)

n, m = map(int, input().split())
matrix = [list(map(int, input().split())) for _ in range(n)]

virus_positive_position = []
for i in range(n):
    for j in range(n):
        if matrix[i][j] == 2:
            virus_positive_position.append([i, j])

ans_list = []
for lst in combinations(virus_positive_position, m):
    visited = [[0 for _ in range(n)] for _ in range(n)]
    BFS(lst)
    virus_check()

if sum(ans_list) == -len(ans_list):
    print(-1)
else:
    min_time = n * n
    for item in ans_list:
        if item > -1 and min_time > item:
            min_time = item

    print(min_time-1)
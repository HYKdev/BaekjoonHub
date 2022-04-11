from collections import deque
import sys
from itertools import combinations

input = sys.stdin.readline

def BFS(virus, deep_m, positive_area):
    global answer
    q = deque()
    for i, j in virus:
        q.append([i, j])
        visited[i][j]= 1
    while q:
        r, c = q.popleft()
        for k in range(4):
            nr = r + dr[k]
            nc = c + dc[k]
            if 0 <= nr < n and 0 <= nc < m and not visited[nr][nc]:
                if not deep_m[nr][nc]:
                    positive_area -= 1
                    visited[nr][nc] = 1
                    q.append([nr, nc])
                    if answer > positive_area:
                        return positive_area
    return positive_area

dr = [0, 0, -1, 1]
dc = [1, -1, 0, 0]

n, m = map(int, input().split())
matrix = [list(map(int, input().split())) for _ in range(n)]

virus_list = []
wall_pos = []
wall_number = 0
for i in range(n):
    for j in range(m):
        if matrix[i][j] == 2:
            virus_list.append([i, j])
        elif matrix[i][j] == 0:
            wall_pos.append([i, j])
            wall_number += 1

answer = 0

for wall_three in combinations(wall_pos, 3):
    visited = [[0 for _ in range(m)] for _ in range(n)]
    deep_matrix = [mat[:] for mat in matrix]
    for i, j in wall_three:
        deep_matrix[i][j] = 1
    cnt = BFS(virus_list, deep_matrix, wall_number)
    if answer < cnt:
        answer = cnt

print(answer-3)
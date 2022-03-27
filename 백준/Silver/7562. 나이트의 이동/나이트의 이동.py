from collections import deque

di = [-1, -2, -2, -1, 1, 2, 2, 1]
dj = [-2, -1, 1, 2, 2, 1, -1, -2]

def BFS(start1, start2):
    q = deque()
    q.append([start1, start2])
    visited[start1][start2] = 1
    while q:
        i, j = q.popleft()
        for k in range(8):
            ni = i + di[k]
            nj = j + dj[k]
            if 0 <= ni < n and 0 <= nj < n:
                if not visited[ni][nj]:
                    visited[ni][nj] = visited[i][j] + 1
                    q.append([ni, nj])
                if ni == r2 and nj == c2:
                    return visited[ni][nj]

T = int(input())
for tc in range(1, T+1):
    n = int(input())
    r1, c1 = map(int, input().split())
    r2, c2 = map(int, input().split())
    visited = [[0 for _ in range(n)] for _ in range(n)]
    if r1 == r2 and c1 == c2:
        print(0)
    else:
        print(BFS(r1, c1)-1)
from collections import deque

di = [0, 0, 1, -1]
dj = [1, -1, 0, 0]

def BFS():
    q = deque()
    q.append([0,0])
    visited = [[0 for _ in range(c)] for _ in range(r)]
    cnt = 0
    while q:
        i, j = q.popleft()
        for k in range(4):
            ni = i + di[k]
            nj = j + dj[k]
            if 0 <= ni < r and 0 <= nj < c:
                if matrix[ni][nj] == 0 and not visited[ni][nj]:
                    q.append([ni,nj])
                    visited[ni][nj] = 1

                elif matrix[ni][nj] == 1:
                    visited[ni][nj] += 1

    for i in range(r):
        for j in range(c):
            if visited[i][j] >= 2:
                cnt += 1
                matrix[i][j] = 0
    
    cheese_list.append(cnt)
    return cnt
# 입력
r, c = map(int, input().split())
matrix = [list(map(int, input().split())) for _ in range(r)]


cheese_list = []

time = 0
while True:
    test_cnt = BFS()
    time += 1
    if test_cnt == 0:
        break

print(time-1)
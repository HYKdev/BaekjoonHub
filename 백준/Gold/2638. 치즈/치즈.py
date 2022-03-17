from collections import deque

di = [0, 0, 1, -1]
dj = [1, -1, 0, 0]

def BFS():
    q = deque()
    visited[0][0] = 1
    q.append([0,0])
    cnt = 0
    while q:
        cnt += 1
        melt_cheese_list = []
        while q:
            i, j = q.pop()
            for k in range(4):
                ni = i + di[k]
                nj = j + dj[k]
                if 0 <= ni < r and 0 <= nj < c:
                    if matrix[ni][nj] == 1 and visited[ni][nj] < 2:
                        visited[ni][nj] += 1
                        if visited[ni][nj] == 2:
                            melt_cheese_list.append([ni,nj])

                    elif matrix[ni][nj] == 0 and visited[ni][nj] == 0:
                        q.append([ni,nj])
                        visited[ni][nj] = 1
        
        for i, j in melt_cheese_list:
            matrix[i][j] = 0
            visited[i][j] = 1

        q = melt_cheese_list

    return cnt-1
# 입력
r, c = map(int, input().split())
matrix = [list(map(int, input().split())) for _ in range(r)]
visited = [[0 for _ in range(c)] for _ in range(r)]

print(BFS())
# 이분 그래프

from collections import deque
import sys

input = sys.stdin.readline

def BFS(start):
    q = deque([start])
    visited[start] = 1

    while q:

        point = q.popleft()

        for grap in graph[point]:
            if not visited[grap]:
                visited[grap] = -1 * visited[point]
                q.append(grap)
            elif visited[point] == visited[grap]:
                return False
    return True
tc = int(input())

for _ in range(tc):
    V, E = map(int, input().split())
    graph = [[] for _ in range(V+1)]
    visited = [0 for _ in range(V+1)]
    for _ in range(E):
        u, v = map(int, input().split())
        graph[u].append(v)
        graph[v].append(u)

    for i in range(1, V+1):
        if not visited[i]:
            result = BFS(i)
            if not result:
                break
    
    print('YES' if result else 'NO')
    
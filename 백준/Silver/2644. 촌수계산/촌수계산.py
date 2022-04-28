from collections import deque

def BFS(start, end):
    q = deque()
    q.append(start)
    visited[start] = 1
    while q:
        i = q.popleft()
        if i == end:
            return visited[i]-1
        for j in graph[i]:
            if not visited[j]:
                visited[j] = visited[i] + 1
                q.append(j)
    return -1
n = int(input())
graph = [[] for _ in range(n+1)]
visited = [0 for _ in range(n+1)]
a, b = map(int, input().split())
m = int(input())

for _ in range(m):
    x, y = map(int, input().split())
    graph[x].append(y)
    graph[y].append(x)

result = BFS(a, b)

print(result)
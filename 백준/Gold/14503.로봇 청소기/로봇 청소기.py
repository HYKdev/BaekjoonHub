dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]


def robot_clean(x, y, d):

    global ans

    if data[x][y] == 0:
        data[x][y] = 2
        ans += 1

    for _ in range(4):
        nd = (d + 3) % 4
        nx = x + dx[nd]
        ny = y + dy[nd]

        if data[nx][ny] == 0:
            robot_clean(nx, ny, nd)
            return

        d = nd

    nd = (d + 2) % 4
    nx = x + dx[nd]
    ny = y + dy[nd]
    if data[nx][ny] == 1:
        return

    robot_clean(nx, ny, d)
            
n, m = map(int, input().split())
x, y, d = map(int, input().split())
data = []
for _ in range(n):
    data.append(list(map(int, input().split())))

ans = 0
robot_clean(x, y, d)

print(ans)
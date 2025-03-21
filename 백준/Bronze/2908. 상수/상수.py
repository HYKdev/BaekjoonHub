x, y = map(str, input().split())

x = int(x[-1]+x[1]+x[0])
y = int(y[-1]+y[1]+y[0])

print(max(x,y))
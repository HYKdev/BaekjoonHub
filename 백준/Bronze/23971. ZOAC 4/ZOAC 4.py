h, w, n, m = map(int, input().split())

n += 1
m += 1
x = 0
y = 0
if h%n:
    x = h//n + 1
else:
    x = h//n

if w%m:
    y = w//m + 1
else:
    y = w//m

print(x*y)
def num_div(n, m):
    while True:
        if m == 0:
            break
        n, m = m, n%m
    return n

n, m = map(int, input().split())


print(num_div(n, m))
print(int(n*m/num_div(n, m)))
t = int(input())

for _ in range(t):
    r, s = map(str, input().split())
    r = int(r)

    ans = ''
    for item in s:
        ans = ans + item * r
    
    print(ans)
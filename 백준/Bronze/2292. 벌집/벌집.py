n = int(input())

numbox = 1
cnt = 1

while True:
    if n <= numbox:
        break
    numbox += 6 * cnt
    cnt += 1

print(cnt)
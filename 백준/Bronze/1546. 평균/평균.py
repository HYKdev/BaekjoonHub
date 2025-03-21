n = int(input())
arr = list(map(int, input().split()))

m = max(arr)

cnt = 0
for num in arr:
    cnt += num/m*100

print(cnt/n)
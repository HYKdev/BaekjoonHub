import sys

n, m = map(int, input().split())

cnt = 0
ans_list = []
n_list = set(sys.stdin.readline().strip() for _ in range(n))

for _ in range(m):
    word = sys.stdin.readline().strip()
    if word in n_list:
        cnt += 1
        ans_list.append(word)

ans_list.sort()
print(cnt)
for ans in ans_list:
    print(ans)
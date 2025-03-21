s = input()

cnt = 0
if len(s) == 1:
    s += s

for i in range(len(s)//2):
    if s[i] == s[-i-1]:
        cnt = 1
    else:
        cnt = 0
        break

print(cnt)

s = input().upper()

arr = [0] * 26

for item in s:
    arr[ord(item)-ord('A')] += 1

max_check = max(arr)

cnt = 0
j = 0
for i in range(len(arr)):
    if arr[i] == max_check:
        cnt += 1
        j = i

if cnt == 1:
    print(chr(65+j))
else:
    print('?')
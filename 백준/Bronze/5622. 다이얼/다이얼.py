s = input()

arr = ['ABC','DEF','GHI','JKL','MNO','PQRS','TUV','WXYZ']

cnt = 0
for item in s:
    for i in range(len(arr)):
        if item in arr[i]:
            cnt += (i+3)

print(cnt)
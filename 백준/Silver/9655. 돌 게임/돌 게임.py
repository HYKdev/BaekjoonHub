n = int(input())

arr = [0] * 1001

arr[1] = 1
arr[2] = 0
arr[3] = 1
for i in range(4,1001):
    if arr[i-1] or arr[i-3]:
        arr[i] = 0
    else:
        arr[i] = 1

if arr[n]:
    print('SK')
else:
    print('CY')
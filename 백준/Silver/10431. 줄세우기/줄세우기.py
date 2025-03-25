n = int(input())

for k in range(n):
    arr = list(map(int, input().split()))
    arr = arr[1:21]
    cnt = 0

    for i in range(20):
        for j in range(i+1,20):
            if arr[i] > arr[j]:
                arr[i],arr[j] = arr[j], arr[i]
                cnt += 1
    
    print(k+1, cnt)



    
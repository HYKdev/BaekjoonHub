N = int(input())

cnt =0
for i in range(1,N-1):
    for j in range(i,N-1):
        k = N-i-j
        if j > k:
            break
        if i+j > k:
            cnt +=1

print(cnt)
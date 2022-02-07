N = int(input())

N_list = list(map(int,input().split()))

cnt = 1
N_max = 1
for i in range(1,N):
    if N_list[i-1] <= N_list[i]:
        cnt += 1
    else:
        cnt = 1
    if N_max < cnt:
        N_max = cnt

cnt = 1
for i in range(1,N):
    if N_list[i-1] >= N_list[i]:
        cnt += 1
    else:
        cnt = 1
    if N_max < cnt:
        N_max = cnt

print(N_max)
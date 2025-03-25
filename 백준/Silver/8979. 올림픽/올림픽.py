n, k = map(int, input().split())

rank_list = []
k_list = []
for _ in range(n):
    arr = list(map(int, input().split()))
    rank_list.append(arr)
    if arr[0] == k:
        k_list = arr

rank_list = sorted(rank_list, key= lambda x: (x[1],x[2],x[3]), reverse=True)

start_num = rank_list.index(k_list)

cnt = start_num + 1

if start_num > 0:
    for i in range(1, start_num):
        if rank_list[start_num][1:] == rank_list[start_num-i][1:]:
            cnt -= 1
        else:
            print(cnt)
            break
    print(cnt)
else:
    print(1)


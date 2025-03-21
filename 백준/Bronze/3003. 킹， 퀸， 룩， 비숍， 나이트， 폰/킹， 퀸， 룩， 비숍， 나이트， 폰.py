check_list = [1, 1, 2, 2, 2, 8]

arr_list = list(map(int, input().split()))

for i in range(len(check_list)):
    if check_list[i] != arr_list[i]:
        print(check_list[i] - arr_list[i], end=" ")
    else:
        print(0, end=" ")
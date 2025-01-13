N = int(input())

num_list = list(map(int, input().split()))

v = int(input())

check_point = 0
for num in num_list:
    if v == num:
        check_point += 1

print(check_point)
N = int(input())
num_list = list(map(int, input().split()))

min_num = 1000000
max_num = -1000000

for num in num_list:
    if num < min_num:
        min_num = num
    
    if num > max_num:
        max_num = num

print(min_num, max_num)
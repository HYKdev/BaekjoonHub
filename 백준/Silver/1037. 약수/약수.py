def number_sort (args):
    for i in range(n):
        for j in range(n-1):
            if args[j] < args[j+1]:
                args[j], args[j+1] = args[j+1], args[j]
    return args

n = int(input())
n_list = list(map(int, input().split()))

number_sort(n_list)

print(n_list[0]*n_list[-1])
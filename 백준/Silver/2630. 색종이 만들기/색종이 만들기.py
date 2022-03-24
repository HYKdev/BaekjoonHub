def check(args, args_n):
    global ans_blue, ans_white

    color_count = 0

    for i in range(args_n):
        color_count += sum(args[i])
    
    if color_count == 0:
        ans_white += 1
    elif color_count == args_n * args_n:
        ans_blue += 1
    else:
        args_temp = [args[i][0:args_n//2] for i in range(0,args_n//2)]
        check(args_temp, args_n//2)
        args_temp = [args[i][0:args_n//2] for i in range(args_n//2, args_n)]
        check(args_temp, args_n//2)
        args_temp = [args[i][args_n//2: args_n] for i in range(0,args_n//2)]
        check(args_temp, args_n//2)
        args_temp = [args[i][args_n//2: args_n] for i in range(args_n//2, args_n)]
        check(args_temp, args_n//2)




n = int(input())
matrix = [list(map(int, input().split())) for _ in range(n)]
visited = [[0 for _ in range(n)] for _ in range(n)]
ans_white = 0
ans_blue = 0

check(matrix, n)
print(ans_white)
print(ans_blue)
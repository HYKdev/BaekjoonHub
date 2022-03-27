def quad_tree(arrs, arrs_n):

    arr_cnt = 0
    for arr in arrs:
        arr_cnt += sum(arr)
    
    if arr_cnt == 0:
        print(0, end='')
    elif arr_cnt == arrs_n*arrs_n:
        print(1, end='')
    else:
        print('(', end='')
        arrs_temp = [arrs[i][0:arrs_n//2] for i in range(0, arrs_n//2)]
        quad_tree(arrs_temp, arrs_n//2)
        arrs_temp = [arrs[i][arrs_n//2: arrs_n] for i in range(0, arrs_n//2)]
        quad_tree(arrs_temp, arrs_n//2)
        arrs_temp = [arrs[i][0:arrs_n//2] for i in range(arrs_n//2, arrs_n)]
        quad_tree(arrs_temp, arrs_n//2)
        arrs_temp = [arrs[i][arrs_n//2:arrs_n] for i in range(arrs_n//2, arrs_n)]
        quad_tree(arrs_temp, arrs_n//2)
        print(')', end='')

n = int(input())

matrix = [list(map(int, input())) for _ in range(n)]

quad_tree(matrix, n)
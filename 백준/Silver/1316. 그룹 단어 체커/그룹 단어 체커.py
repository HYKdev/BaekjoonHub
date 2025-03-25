t = int(input())

cnt = 0
for _ in range(t):
    stack = [[] for _ in range(26)]
    test_string = input()
    ans = True

    for i in range(len(test_string)):
        stack[ord(test_string[i])-ord('a')].append(i)

    for check_stack in stack:
        if len(check_stack) > 1:
            for i in range(len(check_stack)-1):
                if check_stack[i] + 1 != check_stack[i+1]:
                    ans = False
    
    if ans:
        cnt += 1

print(cnt)


    
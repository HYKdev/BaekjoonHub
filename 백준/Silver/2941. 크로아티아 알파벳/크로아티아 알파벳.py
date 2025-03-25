cro_list = ['c=', 'c-', 'dz=', 'd-', 'lj', 'nj', 's=', 'z=']

check_string = input()

cnt = 0
for item in cro_list:
    if item in check_string:
        check_string = check_string.replace(item, "1")

cnt += check_string.count('1')
check_string = check_string.replace('1','')
cnt += len(check_string)

print(cnt)
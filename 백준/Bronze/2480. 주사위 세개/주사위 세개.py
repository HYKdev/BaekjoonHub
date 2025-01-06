a, b, c = map(int, input().split())

check_samepoint = 0

if a == b and b == c:
    check_samepoint = 2

elif ((a == b) and (b != c)) or ((a !=b ) and ( b == c)) or (( a == c ) and ( b != c)):
    check_samepoint = 1

else:
    check_samepoint = 0



if check_samepoint == 2:
    print(10000 + 1000 * a)

elif check_samepoint == 1:
    if a == b:
        print(1000 + 100 * a)
    elif a == c:
        print(1000 + 100 * a)
    elif b == c:
        print(1000 + 100 * b)

else:
    print(max(a,b,c)*100)
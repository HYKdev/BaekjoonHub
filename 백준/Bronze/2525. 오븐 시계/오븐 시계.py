time, minute = map(int, input().split())

cook = int(input())

if minute + cook < 60:
    print(time, minute+cook)

elif minute + cook >= 60:
    check_time = (minute + cook)//60
    check_minute = (minute + cook)%60

    if check_time + time >=24:
        print((check_time+time)%24, check_minute)
    else:
        print(check_time+time, check_minute)

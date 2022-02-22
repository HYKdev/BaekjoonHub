n = int(input())

for i in range(n//2+2):
    if n - 2**i <= 0:
        print(2**i-2*(abs(n-2**i)))
        break
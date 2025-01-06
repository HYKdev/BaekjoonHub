t = int(input())

for i in range(t):
    a, b = map(int, input().split())
    print("Case", f"#{i+1}:", f"{a} + {b} =",a+b)
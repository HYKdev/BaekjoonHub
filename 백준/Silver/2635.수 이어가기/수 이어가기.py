n = int(input())

x = 1
for a in range(n//2,n+1):
    numbers = [n,a]
    i =1

    while True:
        if numbers[i-1] < numbers[i]:
            break
        else:
            numbers.append(numbers[i-1]-numbers[i])
            i+=1

    if x <= len(numbers):
        x = len(numbers)
        numbers_list = numbers

print(x)
for j in range(len(numbers_list)):
    print(numbers_list[j], end=' ')
n = int(input())

arr = []
for _ in range(n):
    word = input()
    arr.append(word)
    
arr = list(set(arr))
arr = sorted(arr, key= lambda x : (len(x), x))

for item in arr:
    print(item)
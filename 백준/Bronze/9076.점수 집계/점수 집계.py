T = int(input())

for _ in range(T):
    scores = list(map(int, input().split()))

    scores.sort()

    scores = scores[1:-1]

    if scores[-1] - scores[0] >=4:
        print('KIN')
    else:
        print(sum(scores))
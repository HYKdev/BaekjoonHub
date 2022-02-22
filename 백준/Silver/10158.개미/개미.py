w, h = map(int, input().split())
j, i = map(int, input().split())
t = int(input())

j_d, j_p = (t+j)//w, (t+j) % w
i_d, i_p = (t+i)//h, (t+i) % h

if j_d % 2 == 0:
    pos1 = j_p
else:
    pos1 = w-j_p

if i_d % 2 == 0:
    pos0 = i_p
else:
    pos0= h-i_p

print(f'{pos1} {pos0}')
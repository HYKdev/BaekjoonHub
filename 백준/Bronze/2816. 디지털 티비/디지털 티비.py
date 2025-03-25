n = int(input())

arr = []
kbs1_idx = 0
kbs2_idx = 0
for i in range(n):
    word = input()
    if word == 'KBS1':
        kbs1_idx += i
    elif word == 'KBS2':
        kbs2_idx += i
    arr.append(word)

if kbs1_idx < kbs2_idx:
    print(kbs1_idx*'1'+kbs1_idx*'4'+kbs2_idx*'1'+(kbs2_idx-1)*'4')
else:
    print(kbs1_idx*'1'+kbs1_idx*'4'+(kbs2_idx+1)*'1'+kbs2_idx*'4')
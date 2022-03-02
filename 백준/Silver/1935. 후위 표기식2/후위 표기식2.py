import sys

n = int(sys.stdin.readline())
alpabet = [0 for _ in range(26)]
arr = sys.stdin.readline().rstrip()

for i in range(n):
    alpabet[i] = int(sys.stdin.readline())

stack = []
for token in arr:
    if token.isalpha():
        stack.append(alpabet[ord(token)-ord('A')])
    else:
        n2 = stack.pop()
        n1 = stack.pop()
        if token == '/':
            stack.append(n1 / n2)
        elif token == '*':
            stack.append(n1 * n2)
        elif token == '+':
            stack.append(n1 + n2)
        elif token == '-':
            stack.append(n1 - n2)

print(format(stack[0], ".2f"))

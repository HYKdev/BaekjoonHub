import sys

word = sys.stdin.readline().strip()

word = sorted(word, reverse=True)

for item in word:
    print(item, end='')
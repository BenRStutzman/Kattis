import sys

best = 0

for i in range(5):
    score = sum([int(num) for num in sys.stdin.readline().split()])
    if score > best:
        winner = i + 1
        best = score

print(winner, best)

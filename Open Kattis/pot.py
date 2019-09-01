import sys

N = int(sys.stdin.readline())
sum = 0

for i in range(N):
    entry = sys.stdin.readline().strip()
    sum += int(entry[:-1]) ** int(entry[-1])

print(sum)

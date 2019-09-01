import sys

n = int(sys.stdin.readline())

temps = [int(num) for num in sys.stdin.readline().split()]

sum = 0

for i in range(n):
    if temps[i] < 0:
        sum += 1

print(sum)

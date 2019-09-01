import sys

N = int(sys.stdin.readline())

for i in range(N):
    num = int(sys.stdin.readline())
    if num % 2:
        print(num, 'is odd')
    else:
        print(num, 'is even')

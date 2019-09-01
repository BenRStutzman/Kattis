import sys

[A, F] = [int(num) for num in sys.stdin.read().split()]

print((F - 1) * A + 1)

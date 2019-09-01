import sys

print(len({int(num) % 42 for num in sys.stdin.read().splitlines()}))

import sys

[num1, num2] = [int(string[::-1]) for string in sys.stdin.read().split()]

print(max(num1, num2))

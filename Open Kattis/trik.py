import sys

loc = 1

moves = sys.stdin.read().split()

for char in moves:
    if char == 'A':
        if loc == 1:
            loc = 2
        elif loc == 2:
            loc = 1
    elif char == 'B':
        if loc == 2:
            loc = 3
        elif loc == 3:
            loc = 2
    else:
        if loc == 1:
            loc = 3
        elif loc == 3:
            loc = 1

print(loc)

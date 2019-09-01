import sys

[hrs, mins] = [int(num) for num in sys.stdin.read().split()]

if mins <= 45:
    mins = mins + 15
    hrs = (hrs - 1) % 24
else:
    mins -= 45

print(hrs, mins)

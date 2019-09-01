import sys
import math

def dist(x1, y1, x2, y2):
    return math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)

def main():
    x, y, x1, y1, x2, y2 = [int(num) for num in input().split()]
    if x1 <= x <= x2:
        print(min(abs(y - y1), abs(y - y2)))
    elif y1 <= y <= y2:
        print(min(abs(x - x1), abs(x - x2)))
    else:
        print(min(dist(x, y, x1, y1), dist(x, y, x1, y2), dist(x, y, x2, y1), dist(x, y, x2, y2)))

main()

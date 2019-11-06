from sys import stdin
import math

def dist(a, b):
    return math.sqrt((a[0] - b[0]) ** 2 + (a[1] - b[1]) ** 2)

def main():
    inp = [[int(num) for num in line.split()] for line in stdin.read().splitlines()]
    pos = [None for i in range(9)]
    for i, row in enumerate(inp):
        for j, item in enumerate(row):
            pos[item - 1] = (i, j)

    total = 0
    for i in range(1, 9):
        total += dist(pos[i - 1], pos[i])
    
    print(total)

main()

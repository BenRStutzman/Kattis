import sys
import math

def main():
    inp = [[float(num) for num in line.split()] for line in sys.stdin.read().splitlines()]
    for line in inp[:-1]:
        print(math.pi * line[0] ** 2, (2 * line[0]) ** 2 * line[2] / line[1])

main()

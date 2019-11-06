from sys import stdin
import math

def main():
    inp = [[int(num) for num in line.split()] for line in stdin.read().splitlines()]


    N = inp[0][0]
    order = [None for i in range(N - 1)]

    for i, between in enumerate(inp[1]):
        order[between] = i + 2

    order = [1] + order
    
    for thing in order:
        print(thing, end = " ")

main()

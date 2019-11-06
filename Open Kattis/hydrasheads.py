from sys import stdin
import math

def main():
    inp = [[int(num) for num in line.split()] for line in stdin.read().splitlines()]
    for H, T in inp[:-1]:
        moves = 0
        while T >= 2:
            T -= 2
            H += 1
            moves += 1
        if T:
            T += 1
            moves += 1
            T -= 2
            H += 1
            moves += 1
        if H % 2:
            moves += 3
            H += 1
        moves += H // 2
        print(moves)

main()

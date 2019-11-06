from sys import stdin
import math

def main():
    inp = [int(num) for num in stdin.readline().strip().split()]
    A, B, C, D = inp
    s = (A + B + C + D) / 2
    print(math.sqrt((s - A) * (s - B) * (s - C) * (s - D)))

main()

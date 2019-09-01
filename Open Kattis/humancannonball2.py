import sys
import math

def main():

    g = 9.81

    inp = [[float(num) for num in line.split()] for line in sys.stdin.read().splitlines()]

    N = int(inp.pop(0)[0])

    for test in range(N):
        [v, th, x, h1, h2] = inp[test]
        th = math.radians(th)
        t = x / (v * math.cos(th))
        y = v * t * math.sin(th) - 0.5 * g * t ** 2
        if h1 + 1 <= y <= h2 - 1:
            print("Safe")
        else:
            print("Not Safe")

main()

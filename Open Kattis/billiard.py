import sys
import math

def main():
    inp = [[float(num) for num in line.split()] for line in sys.stdin.read().splitlines()]
    for w, le, t, v, h in inp[:-1]:
        angle = str(round(180 / math.pi * (math.atan((le * h) / (w * v))), 2))
        if len(angle.split('.')[1]) < 2:
            angle += '0'
        velo = str(round(((le * h) ** 2 + (w * v) ** 2) ** 0.5 / t, 2))
        if len(velo.split('.')[1]) < 2:
            velo += '0'
        print(angle, velo)

main()

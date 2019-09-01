import sys

def main():
    inp  = [[float(num) for num in line.split()] for line in sys.stdin.read().splitlines()]
    for x1, y1, x2, y2, p in inp[:-1]:
        print((abs(x1 - x2) ** p + abs(y1 - y2) ** p) ** (1 / p))
        
main()

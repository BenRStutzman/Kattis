import sys

def main():
    inp  = [[float(num) for num in line.split()] for line in sys.stdin.read().splitlines()]
    N = inp[0][0]
    total = 0
    for ln in inp[1:]:
        total += ln[0] * ln[1]

    print(total)

main()

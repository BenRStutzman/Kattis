import sys
import math

def main():
    rings = [int(num) for num in sys.stdin.read().splitlines()[1].split()]
    R = rings[0]
    for ring in rings[1:]:
        num = R
        den = ring
        while True:
            for i in range(2, min(num, den) + 1):
                if not (num % i or den % i):
                    num //= i
                    den //= i
                    break
            else:
                break
        print("%d/%d" % (num, den))

main()

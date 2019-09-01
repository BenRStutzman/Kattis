import sys
import math

def main():
    inp = [int(num) for num in sys.stdin.read().splitlines()]
    N = inp[0]
    for ln in range(1, N + 1):
        print(math.ceil(inp[ln] / 400))

main()

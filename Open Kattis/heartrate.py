import sys

def main():

    inp = sys.stdin.read().splitlines()
    N = int(inp[0])
    ln = 1

    for i in range(N):
        b, p = [float(num) for num in inp[ln].split()]
        print(60 * (b - 1) / p, 60 * b / p, 60 * (b + 1) / p)
        ln += 1

main()

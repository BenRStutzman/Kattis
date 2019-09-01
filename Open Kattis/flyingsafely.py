import sys

def main():
    inp = sys.stdin.read().splitlines()
    N = int(inp[0])
    ln = 1
    for case in range(N):
        cities, pilots  = [int(num) for num in inp[ln].split()]
        print(cities - 1)
        ln += pilots + 1

main()

import sys

def main():
    inp = sys.stdin.read().splitlines()
    N = int(inp[0])
    won = 0
    for ln in range(1, N + 1):
        if "CD" not in inp[ln]:
            won += 1

    print(won)

main()

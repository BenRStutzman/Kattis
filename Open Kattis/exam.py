import sys

def main():
    inp = sys.stdin.read().splitlines()
    N = int(inp[0])
    num_qs = len(inp[1])
    same = 0
    for i in range(num_qs):
        if inp[1][i] == inp[2][i]:
            same += 1

    print(min(N, same) + (num_qs - same - max(0, N - same)))

main()

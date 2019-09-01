import sys

def main():
    inp = sys.stdin.read().splitlines()
    P, N = [int(num) for num in inp[0].split()]
    replaced = set()
    for ln in range(1, N + 1):
        replaced.add(inp[ln])
        if len(replaced) == P:
            print(ln)
            break
    else:
        print("paradox avoided")

main()

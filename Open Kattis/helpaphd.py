import sys

def main():

    inp = sys.stdin.read().splitlines()
    N = int(inp[0])
    for ln in range(1, N + 1):
        if inp[ln] == "P=NP":
            print("skipped")
        else:
            print(sum([int(num) for num in inp[ln].split('+')]))

main()

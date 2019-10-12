import sys

def main():
    inp = sys.stdin.read().splitlines()
    out = inp[0].split()[1]
    print(out)

main()

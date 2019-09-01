import sys

def main():
    inp = sys.stdin.read().splitlines()
    N = int(inp[0])
    for i, bit in enumerate(inp[1]):
        if (bit == inp[2][i]) == (N % 2):
            print("Deletion failed")
            break
    else:
        print("Deletion succeeded")

main()

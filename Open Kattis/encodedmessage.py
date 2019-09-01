import sys
import math

def main():

    inp = sys.stdin.read().splitlines()
    N = int(inp[0])

    for ln in range(1, N + 1):
        message = inp[ln]
        decoded = ''
        L = len(message)
        root = int(math.sqrt(L))
        for col in range(root - 1, -1, -1):
            for index in range(col, col + (L - root) + 1, root):
                decoded += message[index]
        print(decoded)
            

main()

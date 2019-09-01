import sys

def main():
    inp = sys.stdin.read().splitlines()
    N = int(inp[0])
    start_ln = 1
    for case in range(N):
        print("Test", case + 1)
        R, C = [int(num) for num in inp[start_ln].split()]
        for ln in range(start_ln + R, start_ln, -1):
            print(inp[ln][::-1])

        start_ln += R + 1
    
main()

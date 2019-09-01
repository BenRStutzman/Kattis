import sys

def main():

    inp = sys.stdin.read().splitlines()
    N = int(inp.pop(0))
    for i in range(N):
        print(len(inp[i]))
    
main()

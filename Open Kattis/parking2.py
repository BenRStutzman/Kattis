import sys

def main():

    inp = [[int(num) for num in line.split()] for line in sys.stdin.read().splitlines()]
    N = inp.pop(0)[0]
    for i in range(1, N * 2, 2):
        print(2 * (max(inp[i]) - min(inp[i])))
    
main()

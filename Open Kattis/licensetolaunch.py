import sys

def main():
    inp = [int(num) for num in sys.stdin.read().splitlines()[-1].split()]
    print(inp.index(min(inp)))
    
main()

import sys

def gcd(a, b):
    if b == 0:
        return a
    return gcd(b, a%b)

def main():
    inp = sys.stdin.read().strip().split()
    x, y = int(inp[0]), int(inp[1])
    g = gcd(x, y)
    x = int(x/g)
    y = int(y/g)
    if x%2 == 0 or y%2 == 0:
        print(0)
    else:
        print(g)
    
main()

import sys

def gcd(a, b):
    if b == 0:
        return a
    return gcd(b, a%b)

def main():
    x, y = [int(num) for num in sys.stdin.read().split()]
    g = gcd(x, y)
    x//= g
    y//= g
    if x%2 and y%2:
        print(g)
    else:
        print(0)
    
    
main()

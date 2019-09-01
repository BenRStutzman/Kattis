import sys

def main():
    inp = [[float(num) for num in line.split()] for line in sys.stdin.read().splitlines()]
    N = inp[0][0]
    for ln in inp[1:]:
        b, p = ln
        print((b - 1) * 60 / p, b * 60 / p, (b + 1) * 60 / p)
        
    
    
main()

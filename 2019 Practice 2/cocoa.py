import sys

def main():
    x, y, a = (int(i) for i in sys.stdin.read().strip().split())
    x, y = max(x, y), min(x, y)
    if (a/x == a//x and a/x<=y) or (a/y == a//y and a/y<=x):
        print(1)
        return
    
    for i in range(a//x+1, y+1):
        if (a/i)%1 == 0:
            print(2)
            return

    a = x*y - a
    for i in range(a//x+1, y+1):
        if (a/i)%1 == 0:
            print(2)
            return

    print(3)

main()

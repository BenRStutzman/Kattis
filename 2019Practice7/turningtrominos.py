import sys

def turn(x,y):
    orr = 0
    if (x==y):
        return 0
    for n in range(61,1,-1):
        if (2**(n-2)<=x) and (2**(n-2)<=y) and (3*(2**(n-2))>x) and (3*(2**(n-2))>y):
            x -= 2 ** (n-2)
            y -= 2 ** (n-2)
        elif (x>=2**(n-1)):
            xn = y
            yn = (2**n) - x - 1
            x = xn
            y = yn
            orr -= 1
        elif (y>=2**(n-1)):
            yn = x
            xn = (2**n) - y - 1
            x = xn
            y = yn
            orr += 1
    return orr

def main():
    inp = sys.stdin.read().splitlines()
    lines = inp[1:]
    for line in lines:
        l = line.split()
        print(turn(int(l[0]),int(l[1])))
    


main()

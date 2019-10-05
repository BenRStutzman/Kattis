import sys

def dist(x, y):
    return (x**2+y**2)**0.5

def main():
    inp = sys.stdin.readlines()
    cases = int(inp[0])
    for c in range(cases):
        w,g,h,r = inp[c+1].split()
        w = int(w)
        g = int(g)
        h = int(h)
        r = int(r)
        print(dist(w,g-h), dist(w, g+h-2*r))

main()

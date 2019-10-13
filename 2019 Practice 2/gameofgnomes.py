import sys

def t(n):
    return (n*(n+1))//2

def main():
    put = sys.stdin.read().splitlines()[0].split()
    n = int(put[0])
    m = int(put[1])
    k = int(put[2])
    fk = 0
    gn = n
    while(gn>=m*(k-1)-1):
        gn -= k
        fk += 1
        #print(fk,gn)
    d = t(fk)*k
    d += fk*gn
    x = gn % m
    r = (gn+m-x)//m
    d += r*t(x)
    d += x*(m-x)*(r-1)
    d += (r-1)*t(m-x)
    print(d)




main()

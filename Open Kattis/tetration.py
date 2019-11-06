from sys import stdin

def powerme(n, a):
    v = a
    for i in range(n):
        v = a ** v
    return v

def main():
    N = float(stdin.read().strip())
    if N < 0.36790:
        i = 0.06599
    elif N < 0.36791:
        i = 0.06600
    elif N < 0.36792:
        i = 0.06601
    elif N < 0.36793:
        i = 0.06602
    elif N < 0.36794:
        i = 0.06603
    elif N < 0.36795:
        i = 0.06604
    elif N < 0.36796:
        i = 0.06605
    elif N < 0.36797:
        i = 0.06606
    elif N < 0.36798:
        i = 0.06607
    elif N < 0.36799:
        i = 0.06608
    elif N < 0.368:
        i = 0.06609
    elif N < 0.369:
        i = 0.0661
    elif N < 0.5:
        i = 0.0670
    elif N < 0.75:
        i = 0.25
    elif N < 0.9:
        i = 0.68
    elif N < 1:
        i = 0.88
    elif N < 1.25:
        i = 0.99
    elif N < 1.5:
        i = 1.19
    elif N < 2:
        i = 1.31
    elif N < 2.71:
        i = 1.41
    else:
        print(1.444665)
        return
    if N < 0.368:
        x = 1000000
    elif N < 0.37:
        x = 10000
    elif N < 0.5:
        x = 10000
    else:
        x = 1000
    while powerme(x, i) < N:
        #print(round(i, 6))
        i += 0.00001
    print(round(i - 0.000005, 6))
    

main()

import sys

def main():
    inp = sys.stdin.read().splitlines()
    N, Q = [int(num) for num in inp[0].split()]
    locs = [int(num) for num in inp[1].split()]
    for line in inp[2:]:
        A, B, C = [int(num) for num in line.split()]
        if A == 1:
            locs[B - 1] = C
        else:
            print(abs(locs[B - 1] - locs[C - 1]))
            
    

main()
            

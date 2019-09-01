import sys
import math

def main():
    
    inp = sys.stdin.read().splitlines()

    for ln in inp[:-1]:
        D, V = [float(num) for num in ln.split()]
        R = D / 2
        print(math.pow(R ** 3 - ((3 * V) / (4 * math.pi)), 1/3) * 2)
        
main()

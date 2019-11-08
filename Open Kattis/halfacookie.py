import sys
import math
        

def main():
    inp = [[float(num) for num in line.split()] for line in sys.stdin.read().splitlines()
]
    for r, x, y in inp:
        if x ** 2 + y ** 2 > r ** 2:
            print("miss")
            continue
        b = math.sqrt(x ** 2 + y ** 2)
        h = math.sqrt(r ** 2 - b ** 2)
        #print(b, h)
        A_tri = 0.5 * b * h
        #print(A_tri)
        theta = math.atan2(h, b)
        A_sec = r ** 2 * theta / 2
        #print(theta)
        A_little = 2 * (A_sec - A_tri)
        A_big = math.pi * r ** 2 - A_little
        print(A_big, A_little)     

main()
    

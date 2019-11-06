from sys import stdin
import math

def main():
    inp = [int(num) for num in stdin.read().split()]
    while inp != [1, 2, 3, 4, 5]:
        for i in range(4):
            if inp[i] > inp[i + 1]:
                inp[i:i + 2] = [inp[i + 1], inp[i]]
                print(" ".join([str(num) for num in inp]))
    
main()
        

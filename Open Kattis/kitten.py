from sys import stdin
import math

def main():
    inp = [[int(num) for num in line.split()] for line in stdin.read().splitlines()][:-1]
    cur = inp[0][0]
    while True:
        print(cur, end = " ")
        for line in inp[1:]:
            if cur in line[1:]:
                cur = line[0]
                break
        else:
            break
    
main()
        

from sys import stdin
import math

def main():
    inp = stdin.read().strip()
    to_add = -1
    for char in set(inp):
        if inp.count(char) % 2:
            to_add += 1
    if to_add > 0:
        print(to_add)
    else:
        print(0)
    
main()
        

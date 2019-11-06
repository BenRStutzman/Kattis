from sys import stdin
import math

def main():
    inp = stdin.read().splitlines()
    for line in inp[1:]:
        dim = math.ceil(math.sqrt(len(line)))
        line += '*' * (dim ** 2 - len(line))
        out = ''
        pos = dim ** 2 - dim
        for i in range(dim ** 2):
            if pos < 0:
                pos += dim ** 2 + 1
            if line[pos] != '*':
                out += line[pos]
            pos -= dim
        print(out)
    
main()
        

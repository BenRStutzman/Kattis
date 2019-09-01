import sys

def main():

    inp = sys.stdin.read().splitlines()
    [R, C, H, W] = [int(num) for num in inp.pop(0).split()]
    for line in inp:
        new_line = ''
        for char in line:
            new_line += char * W
        for i in range(H):
            print(new_line)
    
main()

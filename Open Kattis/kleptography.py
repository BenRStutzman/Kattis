import sys

def main():
    alpha = "abcdefghijklmnopqrstuvwxyz"
    inp = sys.stdin.read().splitlines()
    n, m = [int(num) for num in inp[0].split()]
    pt = [alpha.index(char) for char in inp[1]][::-1]
    ct = [alpha.index(char) for char in inp[2]][::-1]
    for i in range(m - n):
        pt.append((ct[i] - pt[i]) % 26)
    pt = "".join([alpha[i] for i in pt])
    print(pt[::-1])

main()
            

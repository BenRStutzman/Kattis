import sys

def main():
    alpha = "abcdefghijklmnopqrstuvwxyz"
    inp = sys.stdin.read().splitlines()
    n, m = [int(num) for num in inp[0].split()]
    print(n, m)
    ct = [alpha.index(char) for char in inp[2]]
    last = [alpha.index(char) for char in inp[1]]
    key = []
    pt = ""
    for i in range(n):
        print(i)
        key.append((ct[-1 - i] - last[-1 - i]) % 26)
    for i in range(m - 1 - n, -1, -1):
        print(i)
        pt += alpha[(ct[i] + key[i % n]) % 26]
    print(pt[::-1] + inp[1])

main()
            

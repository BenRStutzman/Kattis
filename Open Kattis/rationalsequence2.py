import sys

def main():
    inp = [line.split() for line in sys.stdin.read().splitlines()]
    for index, frac in inp[1:]:
        p, q = [int(num) for num in frac.split('/')]
        binary = ''
        while True:
            if p > q:
                p -= q
                binary += '1'
            elif p < q:
                q -= p
                binary += '0'
            else:
                binary += '1'
                break
        print(index, int(binary[::-1], 2))

main()

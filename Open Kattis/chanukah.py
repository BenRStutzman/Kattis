import sys

def main():
    inp = [[int(num) for num in line.split()] for line in sys.stdin.read().splitlines()]
    N = inp[0][0]
    for index, val in inp[1:N + 1]:
        print(index, val * (val + 1) // 2 + val)
        
main()

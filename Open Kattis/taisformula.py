import sys

def main():
    N = int(input())
    inp = [[float(num) for num in line.split()] for line in sys.stdin.read().splitlines()]
    print(sum([(inp[i - 1][1] + inp[i][1]) * (inp[i][0] - inp[i - 1][0]) / 2 for i in range(1, N)]) / 1000)

main()

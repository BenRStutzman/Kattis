import sys

def main():
    inp = sys.stdin.read().splitlines()
    min_max = 50
    best_day = 1
    N = int(inp[0])
    temps = [int(num) for num in inp[1].split()]
    for i in range(N - 2):
        max_temp = max(temps[i], temps[i + 2])
        if max_temp < min_max:
            min_max = max_temp
            best_day = i + 1
    print(best_day, min_max)


main()

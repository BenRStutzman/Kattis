import sys

def main():
    inp = sys.stdin.read().splitlines()
    days = int(inp[0])
    temps = [int(num) for num in inp[1].split()]
    min_max = 100
    day = 0
    for i in range(days - 2):
        max_temp = max(temps[i], temps[i + 2])
        if max_temp < min_max:
            min_max = max_temp
            day = i + 1
    print(day, min_max)

main()

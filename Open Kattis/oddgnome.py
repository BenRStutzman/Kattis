import sys

def main():
    inp = [[int(num) for num in line.split()] for line in sys.stdin.read().splitlines()]
    for line in inp[1:]:
        for i in range(2, line[0]):
            if line[i] > line[i + 1] > line[i - 1] or line[i] < line[i - 1] < line[i + 1]:
                print(i)
                break
main()

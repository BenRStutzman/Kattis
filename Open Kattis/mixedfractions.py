import sys

def main():
    inp = [[int(num) for num in line.split()] for line in sys.stdin.read().splitlines()]
    for line in inp[:-1]:
        print(line[0] // line[1], line[0] % line[1], '/', line[1])

main()

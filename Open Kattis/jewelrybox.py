import sys

def main():
    inp = [[int(num) for num in line.split()] for line in sys.stdin.read().splitlines()]
    for a, b in inp[1:]:
        h = ((4 * (a + b) - (16 * (a + b) ** 2 - 48 * a * b) ** 0.5) / 24)
        print(4 * h ** 3 - 2 * (a + b) * h ** 2 + a * b * h)
    
main()

import sys

def main():
    inp = [[int(num) for num in line.split()] for line in sys.stdin.read().splitlines()[1:]]
    days = set()
    for start, end in inp:
        for i in range(start, end + 1):
            days.add(i)
    print(len(days))

main()

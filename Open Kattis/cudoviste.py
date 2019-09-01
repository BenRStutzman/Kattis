import sys

def main():
    inp = sys.stdin.read().splitlines()
    R, C = [int(num) for num in inp.pop(0).split()]
    inp = [str(line) for line in inp]
    spaces = [0, 0, 0, 0, 0]
    for row in range(R - 1):
        for col in range(C - 1):
            space = inp[row][col:col+2] + (inp[row+1][col:col+2])
            cars_squashed = space.count('X') if '#' not in space else -1
            if cars_squashed >= 0:
                spaces[cars_squashed] += 1

    for entry in spaces:
        print(entry)
main()

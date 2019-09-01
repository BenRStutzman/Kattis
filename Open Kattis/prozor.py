import sys

def main():
    inp = sys.stdin.read().splitlines()
    R, C, S = [int(num) for num in inp.pop(0).split()]
    max_loc = (0, 0)
    max_flies = 0

    for row in range(R - S + 1):
        for col in range(C - S + 1):
            flies = 0
            for r in range(row + 1, row + S - 1):
                flies += inp[r][col + 1:col + S - 1].count('*')
            if flies > max_flies:
                max_flies = flies
                max_loc = (row, col)


    for row in [max_loc[0], max_loc[0] + S - 1]:
        inp[row] = inp[row][:max_loc[1]] + '+' + '-' * (S - 2) + '+' + inp[row][max_loc[1] + S:]
    for row in range(max_loc[0] + 1, max_loc[0] + S - 1):
        inp[row] = inp[row][:max_loc[1]] + '|' + inp[row][max_loc[1] + 1:max_loc[1] + S - 1] + '|' + inp[row][max_loc[1] + S:]

    print(max_flies)
    for row in inp:
        print(row)

main()

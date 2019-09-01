import sys

def main():
    inp = [int(num) for num in sys.stdin.read().splitlines()]
    ln = 0
    first_ln = True
    while True:
        if not first_ln:
            print()
        first_ln = False
        N = inp[ln]
        if not N:
            break
        ln += 1
        first_list = inp[ln:ln + N]
        second_list_sorted = sorted(inp[ln + N:ln + 2 * N])
        first_list_sorted = sorted(first_list)
        for num in first_list:
            print(second_list_sorted[first_list_sorted.index(num)])
        ln += 2 * N
            
main()

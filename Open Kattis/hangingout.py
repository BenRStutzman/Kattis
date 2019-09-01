import sys

def main():

    inp = sys.stdin.read().splitlines()
    L, N = [int(num) for num in inp[0].split()]

    count = 0
    refusals = 0

    for ln in range(1, N + 1):
        action, num = inp[ln].split()
        num = int(num)
        if action == "enter":
            if count + num <= L:
                count += num
            else:
                refusals += 1
        else:
            count -= num

    print(refusals)

main()

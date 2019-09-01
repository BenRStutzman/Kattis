import sys

def main():
    inp = [[int(num) for num in line.split()] for line in sys.stdin.read().splitlines()]
    total = 0
    for index, num in enumerate(inp[1]):
        total += num
        if total > inp[0][1]:
            print(index)
            break
    else:
        print(inp[0][0])

main()

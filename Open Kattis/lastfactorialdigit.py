import sys, math

def main():
    inp = [int(num) for num in sys.stdin.read().splitlines()[1:]]
    for num in inp:
        print(str(math.factorial(num))[-1:])

main()

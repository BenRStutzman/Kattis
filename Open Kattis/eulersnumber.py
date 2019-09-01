import math

def main():
    N = int(input())
    if N > 20:
        print(math.e)
    else:
        e = 0
        for i in range(N + 1):
            e += 1 / math.factorial(i)

        print(e)

main()

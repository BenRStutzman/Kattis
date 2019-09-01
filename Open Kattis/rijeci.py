def numAB(n):
    if n == 0:
        return 1, 0
    last = numAB(n - 1)
    return last[1], sum(last)

def main():
    stuff = numAB(int(input()))
    print(stuff[0], stuff[1])

main()

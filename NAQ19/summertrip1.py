import sys

def main():
    inp = sys.stdin.read().strip()
    N = len(inp)
    total = 0
    i = 0
    while i < N:
        j = i + 1
        while j < N:
            if inp[i] == inp[j]:
                break
            if inp[j] not in inp[i:j]:
                #print(i, j)
                total += 1
            j += 1
        i += 1
    print(total)

main()

def main():
    B, Br, Bs, A, As = [int(num) for num in input().split()]
    print(((Br - B) * Bs) // As + A + 1)

main()

def main():
    N, P, Q = [int(num) for num in input().split()]

    if ((P + Q) // N) % 2:
        print("opponent")
    else:
        print("paul")     

main()

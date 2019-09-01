def main():
    R, C = [int(num) for num in input().split()]
    print(100 * (R - C) ** 2 / R ** 2)

main()

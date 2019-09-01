def main():
    a, b, c = [int(num) for num in input().split()]
    print(max((b - a), (c - b)) - 1)

main()

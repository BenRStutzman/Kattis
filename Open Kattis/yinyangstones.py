def main():
    stones = input()
    if stones.count('B') == stones.count('W'):
        print(1)
    else:
        print(0)

main()

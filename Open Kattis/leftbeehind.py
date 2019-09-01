import sys

def main():
    inp = [[int(num) for num in line.split()] for line in sys.stdin.read().splitlines()]
    for sweet, sour in inp[:-1]:
        if sweet + sour == 13:
            print("Never speak again.")
        elif sweet > sour:
            print("To the convention.")
        elif sweet == sour:
            print("Undecided.")
        else:
            print("Left beehind.")

main()

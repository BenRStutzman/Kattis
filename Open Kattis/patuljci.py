import sys

def main():
    dwarves = [int(num) for num in sys.stdin.read().splitlines()]
    diff = sum(dwarves) - 100
    for i in dwarves:
        for j in dwarves:
            if i != j and i + j == diff:
                dwarves.remove(i)
                dwarves.remove(j)
                for dwarf in dwarves:
                    print(dwarf)
                return

main()

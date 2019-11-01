from sys import stdin
from itertools import product

def main():
    inp = [line.split() for line in stdin.read().splitlines()]
    words = set()
    for line in inp:
        for word in line:
            words.add(word)
    combos = set()
    for A, B in product(words, repeat = 2):
        if A != B:
            combos.add(A + B)
    for word in sorted(combos):
        print(word)

main()

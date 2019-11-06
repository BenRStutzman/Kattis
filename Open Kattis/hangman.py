from sys import stdin
import math

def main():
    word, guess = stdin.read().splitlines()
    letters = set(word)
    misses = 0
    i = 0
    while letters:
        if guess[i] in letters:
            letters.discard(guess[i])
        else:
            misses += 1
            if misses == 10:
                print("LOSE")
                return
        i += 1
    print("WIN")
    return

main()

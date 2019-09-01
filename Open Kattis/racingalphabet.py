import sys
import math

def main():
    inp = sys.stdin.read().splitlines()

    alpha = "ABCDEFGHIJKLMNOPQRSTUVWXYZ '"
    time_per_let = (60 * math.pi / 28) / 15
    #print(time_per_let)

    for line in range(1, int(inp[0]) + 1):
        total_time = 1
        aphorism = inp[line]
        for char_num in range(1, len(aphorism)):
            letters = abs(alpha.index(aphorism[char_num]) - alpha.index(aphorism[char_num - 1])) % 28
            if letters > 14:
                letters = 28 - letters
            total_time += time_per_let * letters + 1
        print(total_time)

main()
        

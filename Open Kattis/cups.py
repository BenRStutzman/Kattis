import sys

def main():

    inp = sys.stdin.read().splitlines()

    N = int(inp[0])
    colors = {}

    for ln in range(1, N + 1):
        part_a, part_b = inp[ln].split()
        if part_a.isalpha():
            colors[int(part_b)] = part_a
        else:
            colors[int(part_a) / 2] = part_b

    for color in sorted(colors):
        print(colors[color])
        
main()

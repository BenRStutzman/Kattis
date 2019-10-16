import sys

def main():
    inp = sys.stdin.read().splitlines()
    N = int(inp[0])
    for i in range(1, 2 * N, 2):
        print("case #%d:" % ((i + 1) / 2), end = " ")
        n = int(inp[i])
        segs = inp[i + 1].split()
        reds = sorted([int(word[:-1]) for word in segs if word.endswith('R')], reverse = True)
        blues = sorted([int(word[:-1]) for word in segs if word.endswith('B')], reverse = True)
        length = 0
        m = min(len(reds), len(blues))
        colors = [reds[:m], blues[:m]]
        if len(colors[1]) == 0:
            print(0)
        else:
            while colors[0]:
                length += colors[0].pop(0) - 1
                colors = colors[::-1]
            print(length)

main()

import sys

def main():
    inp = sys.stdin.read().splitlines()
    N = int(inp[0])
    scores = [0 for i in range(N)]
    results = [""] + inp[1:]
    for i in range(N):
        scores[i] = results[i].count("1") + len([1 for x in range(i + 1, N) if results[x][i] == "0"])
    scores = sorted(scores, reverse = True)
    max_losses = 0
    last_losses = -1
    past = 0
    this_tier = 0
    for score in scores:
        losses = N - 1 - score
        if losses == last_losses:
            this_tier += 1
            if losses - past > max_losses:
                max_losses = losses - past
        else:
            past += this_tier
            this_tier = 1
            last_losses = losses

    print(max_losses * (max_losses + 1) // 2)
            
main()

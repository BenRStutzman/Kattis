import sys

def main():
    inp = sys.stdin.read().splitlines()
    N = int(inp[0])
    scores = [0 for i in range(N)]
    results = [""] + inp[1:]
    for i in range(N):
        scores[i] = results[i].count("1") + len([1 for x in range(i + 1, N) if results[x][i] == "0"])
    losses = sorted([N - 1 - score for score in scores])
    print(losses)
    k = 0
    last_losses = -1
    past = 0
    cur_bad = 0
    last_tier = 0
    for i in range(N):
        if losses[i] == last_losses:
            #print("I:", i)
            if last_tier == 0:
                cur_bad += losses[i] - i
            else:
                cur_bad += losses[i] - losses[last_tier] - (i - last_tier)
        else:
            if last_tier == 0:
                cur_bad = losses[i]
            else:
                cur_bad = losses[i] - losses[last_tier]
            last_tier = i
            last_losses = losses[i]
        if cur_bad > k:
                k = cur_bad
        print(cur_bad)
    print(k)

            
main()

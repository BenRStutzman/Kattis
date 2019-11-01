import sys

def main():
    inp = sys.stdin.read().splitlines()
    N = int(inp[0])
    scores = [0 for i in range(N)]
    results = [""] + inp[1:]
    for i in range(N):
        scores[i] = results[i].count("1") + len([1 for x in range(i + 1, N) if results[x][i] == "0"])
    losses = sorted([N - 1 - score for score in scores])
    #print(losses)
    k = 0
    last_losses = -1
    past = 0
    cur_bad = 0
    last_tier = 0
    on_this_tier = 0
    past = 0
    delayed = 0
    for i in range(N):
        if losses[i] == last_losses:
            on_this_tier += 1
            cur_bad += losses[i] - past - (i - last_tier)
            if delayed:
                past += 1
                delayed = 0
        else:
            if on_this_tier % 2 == 0 and on_this_tier > 1:
                past += on_this_tier - 1
                delayed = 1
            else:
                past += on_this_tier
            on_this_tier = 1
            cur_bad = losses[i] - past
            last_tier = i
            last_losses = losses[i]
        if cur_bad > k:
                k = cur_bad
        print("past", past)
        print("cur_bad", cur_bad)
    print(k)

            
main()

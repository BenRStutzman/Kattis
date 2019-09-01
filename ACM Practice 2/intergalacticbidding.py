import sys

def main():

    inp = sys.stdin.read().splitlines()
    N, S = [int(num) for num in inp[0].split()]
    bids = {int(inp[line].split()[1]): inp[line].split()[0] for line in range(1, N + 1)}

    winners = set()
    for bid in sorted(bids, reverse = True):
        if bid <= S - sum(winners):
            #print(bid)
            winners.add(bid)
            
    if sum(winners) == S:
        print(len(winners))
        for bid in winners:
            print(bids[bid])
    else:
        print(0)

main()

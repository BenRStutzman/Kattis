import sys

def main():
    inp  = [card[0] for card in input().split()]
    ranks = {}
    for rank in inp:
        ranks[rank] = ranks.get(rank, 0) + 1

    print(max(ranks.values()))
    
main()

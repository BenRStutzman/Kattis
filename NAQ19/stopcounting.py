import sys

def highest_avg(N, deck):
    highest_avg = 0
    total = 0
    for i in range(N):
        total += deck[i]
        if total / (i + 1) > highest_avg:
            highest_avg = total / (i + 1)
    return highest_avg

def main():
    inp = sys.stdin.read().splitlines()
    N = int(inp[0])
    cards = [int(num) for num in inp[1].split()]
    
    a1 = highest_avg(N, cards)
    a2 = highest_avg(N, cards[::-1])
    print(max(a1, a2))
    
main()

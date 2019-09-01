import sys

def main():
    inp = [[int(num) for num in line.split()] for line in sys.stdin.read().splitlines()]
    N, K = inp.pop(0)
    team = set()
    for stat in range(3):
        best_pok = sorted([i for i in range(N)], key = lambda pok: inp[pok][stat], reverse = True)
        #print("best_pok:", best_pok)
        team = team.union(set(best_pok[:K]))

    print(len(team))

main()

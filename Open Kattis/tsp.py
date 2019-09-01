import sys

def dist(p1, p2):
    x1, y1 = p1
    x2, y2 = p2
    return ((x2 - x1) ** 2 + (y2 - y1) ** 2) ** 0.5

def main():
    inp = [[float(num) for num in line.split()] for line in sys.stdin.read().splitlines()]
    N = int(inp.pop(0)[0])
    tour = [0]
    used = [True] + [False for i in range(N - 1)]
    #print(tour)
    #print(used)
    for i in range(1, N):
        best = -1
        for j in range(1, N):
            if not used[j] and (best == -1 or dist(inp[tour[-1]], inp[j]) <
                                dist(inp[tour[-1]], inp[best])):
                best = j
        tour.append(best)
        used[best] = True
    #print(tour)
    for stop in tour:
        print(stop)

main()

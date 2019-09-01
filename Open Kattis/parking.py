import sys

def main():
    inp = [[int(num) for num in line.split()] for line in sys.stdin.read().splitlines()]
    costs = [0] + [(i + 1) * inp[0][i] for i in range(3)]
    #print(costs)
    num_trucks = [0 for t in range(max(inp[1][1], inp[2][1], inp[3][1]))]
    for truck_range in inp[1:4]:
        for t in range(truck_range[0], truck_range[1]):
            num_trucks[t] += 1

    #print(num_trucks)

    total_cost = 0
    for t in num_trucks:
        total_cost += costs[t]

    print(total_cost)
            
            
main()

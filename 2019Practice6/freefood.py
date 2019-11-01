import sys

def main():
    inp = sys.stdin.read().splitlines()
    N = int(inp[0])
    ranges = [[int(num) for num in line.split()] for line in inp[1:]]
    #print(ranges)
    all_days = set()
    for entry in ranges:
        for day in range(entry[0], entry[1] + 1):
            all_days.add(day)
    #print(all_days)
    print(len(all_days))
    
main()

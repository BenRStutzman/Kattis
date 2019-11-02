import sys

def main():
    inp = sys.stdin.read().splitlines()
    n = int(inp[0].split()[0])
    locations = [int(i) for i in inp[1].split()]
    lines = [[int(i) for i in line.split()] for line in inp[2:]]
    for line in lines:
        if line[0]==1:
            locations[line[1]-1] = line[2]
        else:
            print(abs(locations[line[1]-1]-locations[line[2]-1]))

    #print(n, locations, lines)




main()

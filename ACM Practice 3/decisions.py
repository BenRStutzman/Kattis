import sys

def main():
    
    inp = sys.stdin.read().splitlines()
    N = int(inp[0])
    vals = [inp[1].split()]
    nodes = 1
    level = 0

    while vals:
        #print(vals)
        new_vals = []
        for group in vals:
            if len(set(group)) == 2:
                nodes += 2
                new_vals.append(group[::2])
                new_vals.append(group[1::2])
        vals = new_vals

    print(nodes)
    
main()

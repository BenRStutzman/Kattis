import sys
        

def main():
    inp = [[int(num) for num in line.split()] for line in sys.stdin.read().splitlines()
]
    min_frac = 1
    canisters = sorted(inp[1])
    for i, v in enumerate(canisters):
        frac = v / (i + 1)
        if frac > 1:
            print("impossible")
            return
        elif frac < min_frac:
            min_frac = frac
    print(min_frac)
        

main()
    

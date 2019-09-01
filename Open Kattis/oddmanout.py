import sys

def main():

    inp = [[int(num) for num in line.split()] for line in sys.stdin.read().splitlines()]
    N = inp.pop(0)[0]

    for ln in range(1, N * 2, 2):
        couples = set()
        for guest in inp[ln]:
            if guest in couples:
                couples.remove(guest)
            else:
                couples.add(guest)
        print("case #%i: %i" % ((ln + 1) / 2, couples.pop()))
                
        
    
main()

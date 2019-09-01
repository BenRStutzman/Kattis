import sys

def main():
    inp = sys.stdin.read().splitlines()[1:]
    inc = True
    dec = True
    i = 1
    while i < len(inp) and (inc or dec):
        if inp[i] > inp[i - 1]:
            dec = False
        elif inp[i] < inp[i - 1]:
            inc = False
        i += 1

    if inc: print("INCREASING")
    elif dec: print("DECREASING")
    else: print("NEITHER")
    
main()

import sys

def main():
    inp  = [[int(num) for num in line.split()] for line in sys.stdin.read().splitlines()]
    case = 1
    for earth, mars in inp:
        print("case %d:" % case)
        #print(earth, mars)
        case += 1
        earth = (365 - earth) % 365
        mars = (687 - mars) % 687
        while earth != mars:
            if earth < mars:
                earth += 365
            else:
                mars += 687
        print(earth)
    
main()

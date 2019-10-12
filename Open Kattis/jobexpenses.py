import sys

def main():
    print(-sum([int(num) for num in sys.stdin.read().splitlines()[1].split() if int(num) < 0]))

main()    

    

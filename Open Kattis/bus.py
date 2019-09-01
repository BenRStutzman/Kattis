import sys

def main():
    inp  = [int(num) for num in sys.stdin.read().splitlines()]

    for num_stops in inp[1:]:
        people = 1
        for stop in range(1, num_stops):
            people *= 2
            people += 1
        print(people)
        
main()

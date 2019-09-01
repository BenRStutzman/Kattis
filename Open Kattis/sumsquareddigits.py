import sys

def main():
    inp = [[int(num) for num in line.split()] for line in sys.stdin.read().splitlines()]
    for index, base, num in inp[1:]:
        SSD = 0
        place = 1
        while num:
            SSD += (num % (place * base)) ** 2
            num //= (place * base)
        print(index, SSD)
        
main()

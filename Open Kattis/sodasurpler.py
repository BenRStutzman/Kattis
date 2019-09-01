import sys

def main():
    
    h, f, c = [int(num) for num in input().split()]
    h += f
    b = 0
    drunk = 0

    while h >= c:
        b = h // c
        h = h % c
        drunk += b
        h += b
        b = 0

    print(drunk)
            
main()

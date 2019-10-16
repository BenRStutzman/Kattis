import sys

def main():
    inp = [int(num) for num in sys.stdin.read().splitlines()]
    N = inp[0]
    for case in inp[1:]:
        order = []
        for i in range(case, 0, -1):
            order.append(i)
            for j in range(i):
                order = order[1:] + [order[0]]
        for card in order[::-1]:
            print(card, end = " ")
        print()
    

main()

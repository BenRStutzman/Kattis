import sys

def main():

    inp = [line.split() for line in sys.stdin.read().splitlines()]
    person = int(inp[0][0])
    N = int(inp[1][0])
    t = 0
    for Q in inp[2:]:
        T, R = int(Q[0]), Q[1]
        if t + T > 210:
            break
        t += T
        person = (person + 1) % 8 if R == 'T' else person

    final_person = person if person else 8
    print(final_person)

    
main()

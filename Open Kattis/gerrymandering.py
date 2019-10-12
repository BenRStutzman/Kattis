import sys

def main():
    inp = sys.stdin.read().splitlines()
    P, D = [int(num) for num in inp[0].split()]
    precincts = [[int(num) for num in line.split()] for line in inp[1:]]
    districts =  [[0,0] for i in range(D)]
    V, W_A, W_B = [0, 0, 0]
    for i, a, b in precincts:
        districts[i - 1][0] += a
        districts[i - 1][1] += b
    for A, B in districts:
        v = A + B
        maj = v // 2 + 1
        if A > B:
            winner = "A"
            w_a = A - maj
            w_b = B
        else:
            winner = "B"
            w_a = A
            w_b = B - maj
        print(winner, w_a, w_b)
        W_A += w_a
        W_B += w_b
        V += v
    print(abs(W_A - W_B)/V)

main()

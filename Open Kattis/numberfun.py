import sys

def main():

    inp = [[int(num) for num in line.split()] for line in sys.stdin.read().splitlines()]
    N = inp.pop(0)[0]

    for ln in range(N):
        [a, b, c] = inp[ln]
        if a + b == c or abs(a - b) == c or a * b == c or a / b == c or b / a == c:
            print("Possible")
        else:
            print("Impossible")            
        
main()

import sys

def main():
    inp = [[float(num) for num in line.split()] for line in sys.stdin.read().splitlines()]
    gunnar = (inp[0][0] + inp[0][1]) / 2 + (inp[0][2] + inp[0][3])/ 2
    emma = (inp[1][0] + inp[1][1]) / 2 + (inp[1][2] + inp[1][3])/ 2
    if gunnar > emma:
        print("Gunnar")
    elif gunnar == emma:
        print("Tie")
    else:
        print("Emma")

main()

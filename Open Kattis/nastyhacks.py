import sys

N = int(sys.stdin.readline())

for i in range(N):
    [no, yes, cost] = [int(num) for num in sys.stdin.readline().split()]
    if yes - no > cost:
        print('advertise')
    elif yes - no == cost:
        print('does not matter')
    else:
        print('do not advertise')

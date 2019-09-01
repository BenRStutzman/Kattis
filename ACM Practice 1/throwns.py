import sys

def main():

    inp = sys.stdin.read().splitlines()
    N, T = [int(num) for num in inp[0].split()]
    commands = inp[1].split()
    cnt = 0
    throws = []
    loc = 0
    for i in range(T):
        if commands[cnt] != 'undo':
            loc = (loc + int(commands[cnt])) % N
            throws.append(int(commands[cnt]))
        else:
            cnt += 1
            for i in range(int(commands[cnt])):
                loc = (loc - throws.pop()) % N
        cnt += 1

    print(loc)

main()

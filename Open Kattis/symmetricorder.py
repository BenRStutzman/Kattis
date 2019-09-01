import sys

def main():

    inp = sys.stdin.read().splitlines()
    ln = 0
    set_num = 1

    while True:
        N = int(inp[ln])
        if N == 0:
            break
        print("SET", set_num)
        ln += 1
        for i in range(0, N, 2):
            print(inp[ln + i])
        for i in range(N - (N % 2 + 1), 0, -2):
            print(inp[ln + i])
        ln += N
        set_num += 1
        
main()

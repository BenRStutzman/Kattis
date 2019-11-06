from sys import stdin, stdout

def main():
    N, H, V = [int(num) for num in stdin.read().strip().split()]
    if H < N / 2:
        H = N - H
    if V < N / 2:
        V = N - V
    out = H * V * 4
    stdout.write(str(out))

main()
